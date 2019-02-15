import os
import random

from django.shortcuts import render, redirect
import requests

try:
    from .api_keys import RAPID_API_KEY

    os.environ['RAPID_API_KEY'] = RAPID_API_KEY
except ImportError:
    pass


# ==== VIEWS =====

def index(request):
    return render(request, 'main_app/index.html')


def redirect_view(request):
    response = redirect('https://www.reddit.com/api/v1/authorize?client_id=QYastqo-s6Y6ZA&response_type=code&state=test&redirect_uri=https://thera-health.herokuapp.com/redirect/&duration=temporary&scope=read')
    testpost = requests.post("https://www.reddit.com/api/v1/access_token")
    return response


# def result(request):
#     ret = {}  # all query types to JSON responses
#     text = request.GET['input']  # get input text from form
#     for query_type in api_urls.keys():
#         json_response = get_api_response(api_urls[query_type], text)
#         ret[query_type] = json_response
#     return render(request, 'main_app/dashboard.html', {'all': ret})


def dashboard(request):
    text = request.GET['input']
    ret = get_quote_and_author(text)
    return render(request, 'main_app/dashboard.html', {'ret': ret})


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
