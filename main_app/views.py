import os
import random
import datetime
import requests
import spotipy
import praw
from spotipy.oauth2 import SpotifyClientCredentials

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.conf import settings

from .forms import UserSignUpForm, UserSignInForm
from .models import User
from .local_api_credentials import spotify_credentials,reddit_credentials

try:
    from .api_keys import RAPID_API_KEY
    os.environ['RAPID_API_KEY'] = RAPID_API_KEY
except ImportError:
    pass


# ==== GENERAL VIEWS =====

def index(request):
    # dt = datetime.datetime.now()
    # formatted_dt =
    return render(request, 'main_app/index.html')


def dashboard(request):
    text = request.GET['input']
    emotion = get_emotion(text)
    # synonym = get_synonym(emotion)
    quote = ("This is demo quote.", "Demo Author")
    music = get_music_url_and_image(emotion)
    ret = {'quote': quote, 'music': music}
    return render(request, 'main_app/dashboard.html', {'ret': ret})


def journal(request, username):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    if request.user.username != username:
        return render(request, 'unavailable.html')
    return render(request, 'main_app/journal.html', {'journal': request.user.journal})


def redirect_view(request):
    response = redirect(
        'https://www.reddit.com/api/v1/authorize?client_id=QYastqo-s6Y6ZA&response_type=code&state=test&redirect_uri=https://thera-health.herokuapp.com/redirect/&duration=temporary&scope=read')
    testpost = requests.post("https://www.reddit.com/api/v1/access_token")
    return response


## === USER AUTHENTICATION ===

def signup(request):
    form = UserSignUpForm(request.POST)
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            new_user = User(first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'],
                            username=form.cleaned_data['username'], password=form.cleaned_data['password'],
                            email=form.cleaned_data['email'])
            new_user.save()
            login(request, new_user)
            render(request, 'main_app/success.html', {'name': new_user.first_name})
    else:
        return render(request, 'main_app/signup.html', {'form': form})


def signin(request):
    form = UserSignInForm()
    return render(request, 'main_app/signin.html', {'form': form})


def signin_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'main_app/dashboard.html', user)
    else:
        return render(request, 'main_app/signin.html')


def signout_view(request):
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


def get_reddit_url(emotion):
    """Get reddit discussion url"""

    client_id,client_secret,user_agent = reddit_credentials
    reddit = praw.Reddit(client_id = client_id,client_secret = client_secret,user_agent = user_agent)

    list_subreddit = ['mademesmile','selfimprovement','GetMotivated']
    choose_random_subreddit = random.choice(list_subreddit)
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
    return 




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
