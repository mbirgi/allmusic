# allmusic

This project scrapes song data from AllMusic and creates a Spotify playlist with the scraped tracks.

## Features

- Scrapes song data from AllMusic
- Searches for tracks on Spotify
- Creates a Spotify playlist and adds the tracks

## Prerequisites

- Python 3.x
- `pip` (Python package installer)
- Spotify Developer Account

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/allmusic.git
    cd allmusic
    ```

2. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

3. Create a [.env](http://_vscodecontentref_/1) file in the project directory and add your Spotify credentials:

    ```env
    SPOTIPY_CLIENT_ID=your_spotify_client_id
    SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
    SPOTIPY_REDIRECT_URI=your_redirect_uri
    ```

## Usage

1. Update the `style` variable in [main.py](http://_vscodecontentref_/2) to the desired music style:

    ```python
    style = 'Clubjazz'  # Change to your desired music style
    ```

2. Run the script:

    ```sh
    python main.py
    ```

3. The script will scrape song data from AllMusic, search for the tracks on Spotify, and create a new playlist with the tracks.

## License

This project is licensed under the MIT License. See the [LICENSE](http://_vscodecontentref_/3) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Acknowledgements

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Spotipy](https://spotipy.readthedocs.io/)
- [dotenv](https://pypi.org/project/python-dotenv/)
