import requests,json,random
text = 'Having a great time coding all night'

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


def analyze_emotion(text):
    #page size can be changed
    base_url = "https://twinword-emotion-analysis-v1.p.rapidapi.com/analyze/?text="
    query = url_encode(text)
    response = requests.get(base_url + query,
        headers={
            "X-RapidAPI-Key": "85a5d7a39emsh30bfd214eaadf58p15822fjsn42e2f79f9778"
        }    
    )
    #print(file['emotions_detected'][0]) <-  get result emotion from the analysis
    return response.json()

def get_associated_word(dict_emo):
    base_url = "https://twinword-word-associations-v1.p.rapidapi.com/associations/?entry="
    emotion = dict_emo['emotions_detected'][0]
    response = requests.get(base_url + emotion,
        headers={
            "X-RapidAPI-Key": "85a5d7a39emsh30bfd214eaadf58p15822fjsn42e2f79f9778"
        }
    )
    assoc_word = response.json()
    #get random word from associated emotion
    random_assoc_word = random.choice(assoc_word['associations_array'])
    return random_assoc_word

def get_article(final_emotion):
    base_url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/WebSearchAPI?autoCorrect=true&pageNumber=1&pageSize=2&"
    query = 'q=' + final_emotion
    response = requests.get(base_url + query + "&safeSearch=true",
        headers={
            "X-RapidAPI-Key": "85a5d7a39emsh30bfd214eaadf58p15822fjsn42e2f79f9778"
        }
    )
    print(final_emotion)
    list_of_article = response.json()
    print(list_of_article)
    return 1







print(get_article(get_associated_word(analyze_emotion(text))))

#len(assoc_word['associations_array'][0])


#response = requests.get("https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/WebSearchAPI?autoCorrect=true&pageNumber=1&pageSize=1&q=coping+happiness&safeSearch=false",
#  headers={
#    "X-RapidAPI-Key": "85a5d7a39emsh30bfd214eaadf58p15822fjsn42e2f79f9778"
#  }
#)

#print(response.json())
