import RPi.GPIO as GPIO
import logging
from time import sleep
import time

logger = logging.getLogger('roomie')

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin-number to which the LED is connected
g_led_pin = 18
print(f'led pin set to: {g_led_pin}')

# Set up the GPIO pin as an output
GPIO.setup(g_led_pin, GPIO.OUT)
logger.debug(f'led pin set to: {g_led_pin}')

################################################################
########################     GPIO    ###########################
################################################################
def change_mode(is_on: bool):
    if is_on:
        GPIO.output(g_led_pin, GPIO.HIGH)
        logger.info("LED ON")
    else:
        GPIO.output(g_led_pin, GPIO.LOW)
        logger.info("LED OFF")


def toggle_led():
    change_mode(not GPIO.input(g_led_pin))


################################################################
########################        PWM     ########################
################################################################
def toggle_pwm_led(duration=5, hz=1):
    """
    Toggle a PWM pin between high and low states for the specified duration.

    Args:
    - pin: GPIO pin number.
    - duration: Total duration (in seconds) to toggle the pin.
    """
    pwm = GPIO.PWM(g_led_pin, 100)  # Create PWM object with frequency 100 Hz
    pwm.start(0)  # Start PWM with 0% duty cycle
    start_time = time.time()
    while time.time() - start_time < duration:
        # Toggle between 0% and 100% duty cycle
        for duty_cycle in [0, 100]:
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(1 / hz)  # Change state every second


def heartbeat_led(duration=10, frequency=1):
    """
    Simulate a smoother heartbeat effect on an LED connected to the specified GPIO pin using PWM.

    Args:
    - pin: GPIO pin number where the LED is connected.
    - duration: Total duration (in seconds) for the heartbeat effect.
    - frequency: Frequency of the heartbeat effect (in Hz).
    """
    # GPIO.setmode(GPIO.BOARD)  # Use board pin numbering
    # GPIO.setup(pin, GPIO.OUT)  # Set pin as output
    logger.debug(f'start heartbit duration {duration}, frequency {frequency}')

    pwm = GPIO.PWM(g_led_pin, frequency * 100)  # Create PWM object with desired frequency
    pwm.start(0)  # Start PWM with 0% duty cycle
    start_time = time.time()
    while time.time() - start_time < duration:
        for duty_cycle in range(0, 101, 5):  # Increase duty cycle gradually
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.1)  # Adjust the time interval for smoother effect
        for duty_cycle in range(100, -1, -5):  # Decrease duty cycle gradually
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.1)  # Adjust the time interval for smoother effect
    pwm.stop()  # Stop PWM
