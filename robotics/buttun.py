import RPi.GPIO as GPIO


def setup_button(callback):
    # GPIO pin connected to the button
    button_pin = 24

    # Set up the button pin as input with a pull-down resistor
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # Add event listener for button press
    GPIO.add_event_detect(button_pin, GPIO.RISING, callback=callback, bouncetime=300)
    print(f'add button listener pin: {button_pin}')

