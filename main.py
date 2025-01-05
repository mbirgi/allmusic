import pprint
from bs4 import BeautifulSoup as bs
import os

pp = pprint.PrettyPrinter(indent=4)

style = 'Clubjazz'  # TODO: avoid hardcoding
folder = 'data'
filename = f'{style} Music Songs _ AllMusic.html'

with open(os.path.join(folder, filename)) as f:
    soup = bs(f, features="html.parser")

track_soup = soup.find('div', class_='descriptorSubGrid')
tracks = []
for row in track_soup.find_all('div', class_='songRow'):
    # print(row.prettify())
    # print('row type: ', type(row))
    track = {}
    track['title'] = row.find('span', class_='songTitle').get_text().strip()
    track['artist'] = row.find('div', class_='songRight').get_text().strip()
    tracks.append(track)
print(tracks[0:3])