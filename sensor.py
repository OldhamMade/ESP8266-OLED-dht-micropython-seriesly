from time import sleep
from dht import DHT22
from machine import Pin

import settings

PIN = Pin(settings.PIN_SENSOR)


def get_data():
    """Return current temp and humidity.

    According to some comments online re. the DHT22,
    to get accurate measurements we need to read
    from the sensor twice, waiting for 2s between
    reads, as some of the data is "cached".
    """
    d = DHT22(PIN)
    d.measure()
    sleep(2)
    d.measure()
    return d.temperature(), d.humidity()
