import time
import RPi.GPIO as GPIO

import spotify_connector.spotify
from robotics.buttun import *
from robotics.led import *

is_playing = False


def on_click(pin):
    print(f"button click! {pin}")
    if is_playing:
        stop()
    else:
        start()


def start():
    global is_playing
    print("start")
    spotify_connector.spotify.start_playlist()
    is_playing = True
    change_mode(is_playing)


def stop():
    global is_playing
    print("stop")
    spotify_connector.spotify.pause_music()
    is_playing = False
    change_mode(is_playing)


def main():
    # Set up GPIO using BCM numbering
    GPIO.setmode(GPIO.BCM)

    # Set up the button
    setup_button(on_click)
    spotify_connector.spotify.get_device()

    try:
        while True:
            time.sleep(2)
            # toggle_led()

    except KeyboardInterrupt:
        # Clean up GPIO on Ctrl+C exit
        GPIO.cleanup()


if __name__ == "__main__":
    main()