import pprint
from bs4 import BeautifulSoup as bs
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

pp = pprint.PrettyPrinter(indent=4)

style = 'Clubjazz'  # TODO: avoid hardcoding
folder = 'data'
filename = f'{style} Music Songs _ AllMusic.html'

with open(os.path.join(folder, filename)) as f:
    soup = bs(f, features="html.parser")

track_soup = soup.find('div', class_='descriptorSubGrid')
tracks = []
for row in track_soup.find_all('div', class_='songRow'):
    track = {}
    track['title'] = row.find('span', class_='songTitle').get_text().strip()
    track['artist'] = row.find('div', class_='songRight').get_text().strip()
    tracks.append(track)

# Spotify credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv('SPOTIPY_CLIENT_ID'),
    client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
    redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
    scope='playlist-modify-public'
))

# Create a new playlist
user_id = sp.current_user()['id']
playlist = sp.user_playlist_create(user_id, f'{style} Allmusic', public=True)
playlist_id = playlist['id']

# Search for tracks and add them to the playlist
for track in tracks:
    query = f"{track['title']} {track['artist']}"
    result = sp.search(query, type='track', limit=1)
    if result['tracks']['items']:
        track_id = result['tracks']['items'][0]['id']
        sp.playlist_add_items(playlist_id, [track_id])

print(f"Tracks added to playlist: {playlist['external_urls']['spotify']}")


