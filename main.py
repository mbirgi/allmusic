import pprint
from bs4 import BeautifulSoup as bs
import os

pp = pprint.PrettyPrinter(indent=4)

style = 'Clubjazz'  # TODO: avoid hardcoding
folder = 'data'
filename = f'{style} Music Songs _ AllMusic.html'

with open(os.path.join(folder, filename)) as f:
    soup = bs(f)

print(soup.prettify())