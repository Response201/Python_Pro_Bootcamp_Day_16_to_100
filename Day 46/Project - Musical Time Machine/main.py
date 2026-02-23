import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
load_dotenv()
from spotipy.oauth2 import SpotifyOAuth
import spotipy

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
BASE_URL = os.getenv("BASE_URL")

# Datum för listan (YYYY-MM-DD)
input_date = "2006-08-12"


# Hämtar HTML från Billboard för ett datum
def get_billboard_list(url):
    try:
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
        response = requests.get(url, headers=header)
        response.raise_for_status()
        list = response.text
        return list
    except requests.RequestException as e:
        print("Error", e)



# Hämtar låttitlar
def get_track_titles():
    list_data=get_billboard_list(f"{BASE_URL}/{input_date}")
    soup = BeautifulSoup(list_data,"html.parser" )
    track_list = soup.select("li ul li h3")
    track_titles = [track.getText(strip=True) for track in track_list]
    return track_titles



# Skapar Spotify-spellista med Billboard-låtar
def create_new_playlist():

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            scope="user-library-read playlist-modify-private",
            redirect_uri=REDIRECT_URI,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET
        )
    )
    user = sp.current_user()
    user_id = user["id"]


    track_titles = get_track_titles()

    # Sök låtar på Spotify
    song_uris = []
    year = input_date.split("-")[0]
    for track in track_titles:
        result = sp.search(q=f"track:{track} year:{year}", type="track")
        print(result)
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{track} doesn't exist in Spotify. Skipped.")

    # Skapa playlist
    playlist = sp.user_playlist_create(user=user_id, name=f"{input_date} Billboard 100", public=False)
    print(playlist)

    # Lägg till låtar
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


create_new_playlist()