import spotipy,json
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

scope = 'user-library-read'
username = 'soda0398'
client_id = 'b584d6ece3834a9fb2de6911d47cb134'
client_secret = '6a35509e8ed8438cb846b39efa103d63'
maneger = SpotifyClientCredentials(client_id = client_id,client_secret = client_secret)
spotify = spotipy.Spotify(client_credentials_manager = maneger)
result = spotify.search(q='anger',limit=1,type='playlist') #<- change happy to emotion


print(result['playlists']['items'][0]['name'])



#for pos in range(4):
#    print(result['playlists']['items'][pos]['external_urls']['spotify'])
#    print(result['playlists']['items'][pos]['images'][0]['url'])