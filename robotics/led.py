import RPi.GPIO as GPIO
import time

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin-number to which the LED is connected
led_pin = 23

# Set up the GPIO pin as an output
GPIO.setup(led_pin, GPIO.OUT)
print(f'led pin set to: {led_pin}')

def change_mode(is_on: bool):
    if is_on:
        GPIO.output(led_pin, GPIO.HIGH)
        print("LED ON")
    else:
        GPIO.output(led_pin, GPIO.LOW)
        print("LED OFF")


def toggle_led():
    change_mode(not GPIO.input(led_pin))
