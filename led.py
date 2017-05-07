from time import sleep
from machine import Pin

pin = Pin(2)
pin.init(Pin.OUT)


def blink(timeout=None):
    """Blink the onboard LED for the specified time.

    If no time is specified, the LED will stay switched on.
    """
    pin.low()
    if timeout:
        sleep(timeout)
        pin.high()
