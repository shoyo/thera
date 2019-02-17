import os
import random
import requests
import spotipy
import praw
from spotipy.oauth2 import SpotifyClientCredentials

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf import settings

from .forms import UserSignUpForm, UserSignInForm
from .models import User, JournalEntry
from .local_api_credentials import spotify_credentials,reddit_credentials, doctor_credentials

try:
    from .api_keys import RAPID_API_KEY
    os.environ['RAPID_API_KEY'] = RAPID_API_KEY
except ImportError:
    pass


# ==== GENERAL VIEWS =====

def index(request):
    return render(request, 'main_app/index.html')


def dashboard(request):
    try:
        text = request.GET['input']
    except KeyError:
        text = "happy"
    polarity = get_polarity(text)
    emotion = get_emotion(text)
    synonym = get_synonym(emotion)
    quote = get_quote_and_author(emotion)
    music = get_music_url_and_image(emotion)
    reddit_info = get_reddit_url()
    getting_help(request)
    ret = {'quote': quote, 'music': music, 'polarity': polarity,'reddit':reddit_info}
    return render(request, 'main_app/dashboard.html', {'ret': ret})

def getting_help(request):
    experts = get_experts()
    return render(request, 'main_app/getting_help.html', {'experts': experts})


## === USER AUTHENTICATION ===



def logout_view(request):
    logout(request)
    return render(request, 'main_app/index.html')


## ===========================


# ==========

api_urls = {
    'sentiment': 'https://aylien-text.p.rapidapi.com/sentiment?text=',
    'emotion': 'https://twinword-emotion-analysis-v1.p.rapidapi.com/analyze/?text=',
    'synonym': 'https://twinword-word-associations-v1.p.rapidapi.com/associations/?entry=',
    'article': 'https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/WebSearchAPI?autoCorrect=true&pageNumber=1&pageSize=2&',
    'quote': 'https://theysaidso.p.rapidapi.com/quote?category=',
}


## Specific helper functions (used to obtain specific data)

def get_polarity(text):
    """Return the polarity (1 for positive, -1 for negative, 0 for neutral) of the given text."""
    json_response = get_api_response(api_urls['sentiment'], text)
    polarity = json_response['polarity']
    if polarity == 'positive':
        return 1
    elif polarity == 'negative':
        return -1
    else:
        return 0

def get_emotion(text):
    """Return the emotion with the highest probability for the given text."""
    json_response = get_api_response(api_urls['emotion'], text)
    response = json_response['emotion_scores']
    return max(response, key=response.get)


def get_synonym(word):
    """Return a random synonym of word. Used to randomize search query."""
    json_response = get_api_response(api_urls['synonym'], word)
    return random.choice(json_response['associations_array'])


def get_article_url(emotion):
    """Return an article url associated with given emotion."""
    json_response = get_api_response(api_urls['article'], emotion)
    return json_response['value']


def get_quote_and_author(category):
    """Return tuple of a quote associated with given categoryand its author."""
    json_response = get_api_response(api_urls['quote'], category)
    return json_response['contents']['quote'], json_response['contents']['author']


def get_music_url_and_image(emotion):
    """Return Spotify playlist data for a given emotion.

    Response format example (when ret_count = 4):
    [(playlist_1_url, playlist_1_img, playlist_1_title),
    (playlist_2_url, playlist_2_img, playlist_2_title),
    (playlist_3_url, playlist_3_img, playlist_3_title),
    (playlist_4_url, playlist_4_img, playlist_4_title)]
    """
    ret = []
    ret_count = 4
    username, client_id, client_secret = spotify_credentials
    manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    spotify = spotipy.Spotify(client_credentials_manager=manager)
    response = spotify.search(q=emotion, limit=ret_count, type='playlist')
    for i in range(ret_count):
        url = response['playlists']['items'][i]['external_urls']['spotify']
        image = response['playlists']['items'][i]['images'][0]['url']
        title = response['playlists']['items'][i]['name']
        ret.append((url, image, title))
    return ret


def get_reddit_url():
    """Get reddit discussion url"""
    store_link = [] #stores 4 subreddit link
    client_id,client_secret,user_agent = reddit_credentials
    reddit = praw.Reddit(client_id = client_id,client_secret = client_secret,user_agent = user_agent)

    list_subreddit = ['mademesmile','selfimprovement','GetMotivated','faithinhumanity']
    rand_subreddit = random.choice(list_subreddit)
    for submission in reddit.subreddit(rand_subreddit).hot(limit=4):
        post_id = submission.id
        post_title = submission.title
        store = []
        for chara in post_title:
            if chara == ' ' :
                store.append('_')
            else:
                store.append(chara)
        post_title = ''.join(store)
        post_title = post_title.replace('[','')
        post_title = post_title.replace(']','')
        post_title = post_title.lower()
        url = 'https://reddit.com/r/' + rand_subreddit + '/comments/' + post_id + '/' + post_title
        store_link.append((submission.title,url))
    return store_link


def get_experts():
    """Get doctor data"""
    doctor_info_dict = []
    response = requests.get("https://moocher-io-ip-geolocation-v1.p.rapidapi.com/104.247.134.239",
        headers={
            "X-RapidAPI-Key": 'ff1d2d95d4msh535c8f00c27ed89p140640jsn0918e6dccb33'
        }
    )
    doctor_api_key = doctor_credentials
    location = response.json()
    latitude = float(location['ip']['latitude'])
    longitude = float(location['ip']['longitude'])
    loc = 'location=' + str(latitude) + '%2C' + str(longitude)
    query = 'https://api.betterdoctor.com/2016-03-01/practices?'+loc+'%2C100&user_location='+str(latitude)+'%2C'+str(longitude)+'&skip=0&limit=3&user_key='+doctor_api_key
    find_doc = requests.get(query)
    result = find_doc.json()
    for pos in range(len(result['data'])):
        if result['data'][pos]['total_doctors'] == 0:
            pass
        else:
            name =result['data'][pos]['doctors'][0]['profile']['first_name'] + ' '+result['data'][pos]['doctors'][0]['profile']['last_name']
            url_img = result['data'][pos]['doctors'][0]['profile']['image_url']
            specialty = result['data'][pos]['doctors'][0]['specialties'][0]['description']
            city = result['data'][pos]['visit_address']['city']
            state = result['data'][pos]['visit_address']['state']
            doctor_info_dict.append((name,url_img,specialty,city,state))
            #print(name,url_img,specialty,state,'-',city)
    return doctor_info_dict

def doctor(ip_address):
    """Get doctor data"""
    doctor_info_dict = {}
    response = requests.get("https://moocher-io-ip-geolocation-v1.p.rapidapi.com/192.119.168.96",
        headers={
            "X-RapidAPI-Key": "85a5d7a39emsh30bfd214eaadf58p15822fjsn42e2f79f9778"
        }
    )
    doctor_api_key = doctor_credentials
    location = response.json()
    latitude = float(location['ip']['latitude'])
    longitude = float(location['ip']['longitude'])
    query = 'https://api.betterdoctor.com/2016-03-01/practices?'+loc+'%2C100&user_location='+str(latitude)+'%2C'+str(longitude)+'&skip=0&limit=3&user_key='+api_key
    find_doc = requests.get(query)
    for pos in range(len(result['data'])):
        if result['data'][pos]['total_doctors'] == 0:
            pass
        else:
            name =result['data'][pos]['doctors'][0]['profile']['first_name'] + result['data'][pos]['doctors'][0]['profile']['last_name']
            url_img = result['data'][pos]['doctors'][0]['profile']['image_url']
            specialty = result['data'][pos]['doctors'][0]['specialties'][0]['description']
            city = result['data'][pos]['visit_address']['city']
            state = result['data'][pos]['visit_address']['state']
            doctor_info_dict[name] = []
            doctor_info_dict[name].extend((url_img,specialty,city,state))
            #print(name,url_img,specialty,state,'-',city)
    return doctor_info_dict




## General helper functions (used in every API call)

def get_api_response(api_base_url, text):
    """Return JSON response from API base url given the input text."""
    query = url_encode(text)
    response = requests.get(api_base_url + query,
                            headers={"X-RapidAPI-Key": os.environ['RAPID_API_KEY']})
    return response.json()


def url_encode(text):
    """Return a processed version of text for API query."""
    ret = []
    for letter in text:
        if letter == ' ':
            new = '+'
        elif letter == ',':
            new = '%2C'
        else:
            new = letter
        ret.append(new)
    return ''.join(ret)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return HttpResponse(ip)
