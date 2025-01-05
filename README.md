# allmusic

This project uses an html file saved from AllMusic containing the top songs for a genre and creates a Spotify playlist with the tracks.

## Features

- Reads song data from an html file
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

3. Create a [.env] file in the project directory and add your Spotify credentials:

    ```env
    SPOTIPY_CLIENT_ID=your_spotify_client_id
    SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
    SPOTIPY_REDIRECT_URI=your_redirect_uri
    ```

## Usage

1. Save the page with the desired genres top songs (e.g. https://www.allmusic.com/style/clubjazz-ma0000011890/songs) to the data directory in the format `{style} Music Songs _ AllMusic.html`

2. Update the `style` variable in [main.py] to the desired music style:

    ```python
    style = 'Clubjazz'  # Change to your desired music style
    ```

3. Run the script:

    ```sh
    python main.py
    ```

4. The script will read the song data from the saved file, search for the tracks on Spotify, and create a new playlist with the tracks.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE] file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Acknowledgements

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Spotipy](https://spotipy.readthedocs.io/)
- [dotenv](https://pypi.org/project/python-dotenv/)
