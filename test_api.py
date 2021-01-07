import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = "0afdbf72f4be4dcba460a145fb3d827d"
secret = "422dddd63d794cb8ba3fc8f45c90fa1a"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

# First need to get "User Authorization" from HTTP endpoint to be able to see their friends list, what their friends (user) is currently playing
# and be able to play songs on their behalf 

#Main Feature: 
#Once that's done - we can then use the "Get the User's Currently Playing Track" 

#Then simply play the song at the timestamp once retrieved from JSON package 

#If user changes song - retrieve new song - play new song at timestamp 


#Extra Feature: 
#Recall API every X seconds to see if their time has changed substantially (by some ~10 sec threshold) - if so, then skip the song to that time stamp. 
