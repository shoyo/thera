import os
from django.shortcuts import render
import requests
try:
    from .api_keys import RAPID_API_KEY
    os.environ['RAPID_API_KEY'] = RAPID_API_KEY
except ImportError:
    pass

# Create your views here.

def index(request):
    return render(request, 'main_app/index.html')


def result(request):
    text = request.GET['input']
    ret = {'data': analyze_sentiment(text)}
    return render(request, 'main_app/result.html', ret)


# Helper functions

def analyze_sentiment(text):
    """Return dictionary containing sentiment data of text."""
    base_url = 'https://aylien-text.p.rapidapi.com/sentiment?text='
    query = url_encode(text)
    response = requests.get(base_url + query,
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
