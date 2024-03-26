import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import socket
import subprocess
import time

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=['user-library-read',
                                                      "app-remote-control",
                                                      "user-read-playback-state",
                                                      "user-modify-playback-state"]))
g_device_id = None
disney_baby_uri = "0O2NkHCJE31kRyK7lX58A6"


def get_spotify_device_id(name: str):
    for device in sp.devices()['devices']:
        if device['name'] == name:
            return device['id']

    return None


def get_device():
    global g_device_id
    hostname = socket.gethostname()
    print("device Hostname:", hostname)

    device_id = get_spotify_device_id(hostname)
    if device_id is None:
        print(f"my device was not found, try open chrome")
        command = ['chromium-browser', '--new-window', "https://open.spotify.com/"]
        subprocess.Popen(command)
        while device_id is None:
            device_id = get_spotify_device_id('Web Player (Chrome)')

    g_device_id = device_id
    print(f"device is id: {hostname}")


def start_playlist(playlist_uri=f'spotify:playlist:{disney_baby_uri}'):
    print(f'starting playlist {playlist_uri}')
    sp.start_playback(device_id=g_device_id, context_uri=playlist_uri)


def pause_music():
    print(f'pausing playlist')
    sp.pause_playback(g_device_id)


if __name__ == "__main__":
    get_device()
    start_playlist()