from network import WLAN, STA_IF
from logging import getLogger

import settings

log = getLogger(__name__)
net = None


def connect():
    """Connect to the local wifi network."""
    global net
    net = WLAN(STA_IF)
    if not net.isconnected():
        log.warn("no network, attempting to connect to %s", settings.WIFI_SSID)
        net.active(True)
        net.connect(settings.WIFI_SSID, settings.WIFI_PW)
        while not net.isconnected():
            pass
    status()


def status():
    """Log the status of the wifi connection."""
    try:
        log.info('network config: %s', net.ifconfig())
    except AttributeError:
        log.warn('network not connected')
