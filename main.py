import time
import spotify_connector.spotify
from robotics.buttun import *
from robotics.led import *
import os
import random


logger = logging.getLogger('roomie')
is_playing = False


def create_directory(path):
    """
    Create a directory path if it doesn't exist.
    """
    if not os.path.exists(path):
        os.makedirs(path)


def on_click(pin):
    logger.debug(f"button click! {pin}")
    if is_playing:
        stop()
    else:
        start()


def start():
    global is_playing
    logger.debug("start")
    spotify_connector.spotify.start_playlist()
    is_playing = True


def stop():
    global is_playing
    logger.debug("stop")
    spotify_connector.spotify.pause_music()
    is_playing = False


def handle_log():
    log_file_path = "log"
    create_directory(log_file_path)
    log_file_name = "rommie.log"
    file_path = os.path.join(log_file_path, log_file_name)

    # Create a logger and set its level to DEBUG
    logger = logging.getLogger('roomie')
    logger.setLevel(logging.DEBUG)

    # Create a formatter for the log messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create a file handler that writes to the specified log file
    file_handler = logging.FileHandler(file_path)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    # logger.addHandler(file_handler)

    # Create a console handler that writes to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


def main():
    handle_log()
    spotify_connector.spotify.get_device()

    # Set up GPIO using BCM numbering
    GPIO.setmode(GPIO.BCM)

    # Set up the button
    setup_button(on_click)

    try:
        while True:
            if not is_playing:
                heartbeat_led(duration=2, frequency=2)
            else:
                heartbeat_led(duration=random.randint(1, 5), frequency=random.randint(1, 10))
    except KeyboardInterrupt:
        # Clean up GPIO on Ctrl+C exit
        GPIO.cleanup()


if __name__ == "__main__":
    main()