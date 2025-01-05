import pprint
from bs4 import BeautifulSoup as bs
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

# Ensure the logs directory exists
os.makedirs('logs', exist_ok=True)

# Set up logging to a file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)

pp = pprint.PrettyPrinter(indent=4)

style = 'Jazz-House'  # TODO: avoid hardcoding
folder = 'data'
filename = f'{style} Music Songs _ AllMusic.html'

logging.info(f'Opening file: {filename}')
with open(os.path.join(folder, filename)) as f:
    soup = bs(f, features="html.parser")

logging.info('Parsing HTML content')
track_soup = soup.find('div', class_='descriptorSubGrid')
tracks = []
for row in track_soup.find_all('div', class_='songRow'):
    track = {}
    track['title'] = row.find('span', class_='songTitle').get_text().strip()
    track['artist'] = row.find('div', class_='songRight').get_text().strip()
    tracks.append(track)

logging.info(f'Found {len(tracks)} tracks')

# Spotify credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv('SPOTIPY_CLIENT_ID'),
    client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
    redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
    scope='playlist-modify-public'
))

# Check if playlist already exists
user_id = sp.current_user()['id']
playlists = sp.user_playlists(user_id)
playlist_id = None

for playlist in playlists['items']:
    if playlist['name'] == f'{style} Allmusic':
        playlist_id = playlist['id']
        logging.info(f'Found existing playlist: {playlist["name"]} with ID: {playlist_id}')
        break

if playlist_id:
    # Clear existing playlist
    sp.playlist_replace_items(playlist_id, [])
    logging.info(f'Cleared existing playlist: {playlist["name"]}')
else:
    # Create a new playlist
    playlist = sp.user_playlist_create(user_id, f'{style} Allmusic', public=True)
    playlist_id = playlist['id']
    logging.info(f'Created new playlist: {playlist["name"]} with ID: {playlist_id}')

# Search for tracks and add them to the playlist
tracks_added = 0
for track in tracks:
    query = f"{track['title']} {track['artist']}"
    result = sp.search(query, type='track', limit=1)
    if result['tracks']['items']:
        track_id = result['tracks']['items'][0]['id']
        sp.playlist_add_items(playlist_id, [track_id])
        tracks_added += 1
    else:
        logging.warning(f'Track not found: {track["title"]} by {track["artist"]}')

logging.info(f'Added {tracks_added} tracks to playlist: {playlist["external_urls"]["spotify"]}')
logging.info('**** Done ****')

