from ssd1306 import SSD1306_I2C
from machine import I2C, Pin

import settings

SDA = Pin(settings.PIN_SDA)
SCL = Pin(settings.PIN_SCL)
SCREEN = SSD1306_I2C(
    settings.OLED_WIDTH,
    settings.OLED_HEIGHT,
    I2C(sda=SDA, scl=SCL)
)


def display(location, temperature, humidity):
    SCREEN.fill(0)

    SCREEN.text(location, 0, 0)

    temp = '{:.1f}'.format(temperature)
    SCREEN.text('T:', 0, 20)
    SCREEN.text(temp, 20, 20)

    hmdty = '{:.1f}'.format(humidity)
    SCREEN.text('H:', 0, 40)
    SCREEN.text(hmdty, 20, 40)

    SCREEN.show()


def welcome():
    SCREEN.fill(0)
    SCREEN.text('ONLINE', 7, 20)
    SCREEN.show()


def error():
    SCREEN.fill(0)
    SCREEN.text('ERROR', 11, 20)
    SCREEN.show()
