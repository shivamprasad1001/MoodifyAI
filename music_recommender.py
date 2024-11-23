import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
import os

client_id = os.getenv("spotify_client_id")
client_secret = os.getenv("spotify_client_secret")
# Set up Spotify credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
))


def get_music_recommendations(emotion):
    mood_to_genre = {
        "Happy": "pop",
        "Sad": "acoustic",
        "Angry": "rock",
        "Relaxed": "chill"
    }
    genre = mood_to_genre.get(emotion, "pop")
    offset = random.randint(0, 990)  
    results =    sp.search(q=f"genre:{genre}", type="track", limit=10, offset=offset)
    # results = sp.search(q=f"genre:{genre}", type="track", limit=10)
    songs = []
    for track in results['tracks']['items']:
        songs.append({
            "name": track['name'],
            "artist": track['artists'][0]['name'],
            "url": track['external_urls']['spotify'],
            "image_url":track['album']['images'][0]['url']
        })
    return songs