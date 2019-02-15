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


# def result(request):
#     text = request.GET['input']
#     ret = {'data': analyze_sentiment(text)}
#     return render(request, 'main_app/result.html', ret)

def result(request):
    ret = {} # all query types to JSON responses
    query2url = {
        # query type to base URL
        'sentiment': 'https://aylien-text.p.rapidapi.com/sentiment?text=',
        'emotion': 'https://twinword-emotion-analysis-v1.p.rapidapi.com/analyze/?text=',
    }
    text = request.GET['input'] # get input text from form
    for query_type in query2url.keys():
        json_response = get_api_response(query2url[query_type], text)
        ret[query_type] = json_response
    return render(request, 'main_app/result.html', {'all': ret})


# Helper functions

# def get_emotion()

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
