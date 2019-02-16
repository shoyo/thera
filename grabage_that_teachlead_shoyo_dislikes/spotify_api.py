import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

def redirect_spotify(request):
    scope = 'user-library-read'
    username = 'soda0398'
    client_id = 'b584d6ece3834a9fb2de6911d47cb134'
    client_secret = '6a35509e8ed8438cb846b39efa103d63'
    maneger = SpotifyClientCredentials(client_id = client_id,client_secret = client_secret)
    spotify = spotipy.Spotify(client_credentials_manager = maneger)
    result = spotify.search(q='happy',limit=1,type='playlist')



    return HttpResponse(result['playlists']['items'][0]['external_urls']['spotify'])