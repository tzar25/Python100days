from bs4 import BeautifulSoup
import requests
from os import getenv
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv(override=True)

SPOTIFY_ID = getenv("SPOTIFY_ID")
SPOTIFY_SECRET = getenv("SPOTIFY_SECRET")

# Scraping from Billboard
date = input("Type the year you want the hottest songs of in the format YYYY-MM-DD: ")
# date = "1990-02-17"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get(url="https://www.billboard.com/charts/hot-100/" + date, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_selection = soup.select("li ul li h3")
authors_selection = soup.select("li ul li span")

song_names = [song.getText().strip() for song in song_names_selection]
author_names = [author.getText().strip() for author in authors_selection][::7]


# Spotify setup
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        redirect_uri="https://www.example.com",
        scope="playlist-modify-private",
        cache_path=".cache"))

user_id = sp.current_user()["id"]

playlist = sp.user_playlist_create(user_id, f"Billboard hot 100 - {date}", public=False, collaborative=False, description='')
list_id = playlist["id"]

tracks = []

for i in range(100):
    song = song_names[i]
    author = author_names[i]
    query = f"track:{song} artist:{author}"

    search_result = sp.search(q=query, limit=1, type='track')
    # print(search_result)
    try:
        track_uri = search_result['tracks']['items'][0]['uri']
        print(f"List: {list_id}, Track: {track_uri}. Added {song} by {author}.")
        tracks.append(track_uri)
    except IndexError:
        print(f"Track: {song} by author: {author} not found. Retrying with only the song name.", end=" ")
        query = f"track:{song}"
        search_result = sp.search(q=query, limit=1, type='track')
        try:
            track_uri = search_result['tracks']['items'][0]['uri']
            print(f"List: {list_id}, Track: {track_uri}")
            tracks.append(track_uri)
        except IndexError:
            print("Still not found. Skipping over.")
            continue

sp.playlist_add_items(playlist_id=list_id, items=tracks)
