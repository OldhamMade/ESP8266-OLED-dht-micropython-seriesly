import gc
import micropython

from esp import sleep_type as esp_sleep_type, SLEEP_NONE, SLEEP_LIGHT
from os import listdir
from json import dumps as json_dump
from time import sleep as time_sleep
from urequests import post

from logging import getLogger

import settings
import wifi
import sensor
import display

micropython.alloc_emergency_exception_buf(100)
gc.collect()  # clean up mem after imports

log = getLogger(__name__)


def conditionally_enable_webrepl():
    """Enable the webrepl if trigger file `webrepl_on` is found in the root."""
    if 'webrepl_on' in listdir():
        from webrepl import start
        start()
        gc.collect()


def publish():
    """Publish sensor and memory details to Seriesly."""
    temperature, humidity = sensor.get_data()

    data = json_dump({
        'location': settings.LOCATION.lower(),
        'temperature': temperature,
        'humidity': humidity,
        'gc_mem_free': gc.mem_free(),

    })

    resp = post(
        settings.DB_URI,
        data=data
    )

    status = resp.status_code

    resp.close()

    if status != 201:
        log.warn('could not store %s', data)
        display.error()
        return False

    log.info('successfully stored %s', data)
    display.display(settings.LOCATION, temperature, humidity)
    return True


def execute():
    """Wake, connect to nwifi, publish details, and go back to sleep."""
    gc.collect()
    esp_sleep_type(SLEEP_NONE)
    wifi.connect()
    publish()
    esp_sleep_type(SLEEP_LIGHT)
    time_sleep(settings.SLEEP_INTERVAL)


def log_exception(e):
    """Capture log information to a file for later review."""
    with open('error.log', 'a') as f:
        f.write(str(e))


def main():
    """Main loop."""
    display.welcome()
    conditionally_enable_webrepl()
    while True:
        try:
            execute()
        except Exception as e:
            log_exception(e)


if __name__ == '__main__':
    main()
