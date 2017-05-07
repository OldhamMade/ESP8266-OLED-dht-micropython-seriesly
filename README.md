# Temperature/Humidity Display using MicroPython and Seriesly

A small project to display and send temperature and humidity information
to the timeseries database [Seriesly][1] for later study. Built
for ESP8266/Wemos-D1 boards running MicroPython.

![Example Image][example_image]

## Hardware

For this project, I used the following items:

- [Wemos D1 mini pro][6]
- [Wemos DHT Pro shield][7]
- [Wemos OLED shield][8]

## Installing MicroPython

You'll need to install the correct drivers for your OS and board. You should
then be able to proceed by following the [MicroPython install instructions][3].

## Installing the code

The easiest way to do this is to connect to the board using something like
[picocom][4], enable the `webrepl`, and use the [MicroPython webrepl tool][5]
to upload the files to the board. Remember to update the `settings.py` file
as necessary with network and pin settings before uploading.

I can also recomment using [adafruit-ampy][9] if you prefer transferring files
directly over your wired connection.

Once you've installed the dependencies, rebooting the board should kick things
off and you should immediately see an `ONLINE` message on your OLED display,
followed by some temperature/humidity readings, and entries should start
appearing in your Seriesly server.

### Dependencies
Before the code will run, you'll need to install the dependencies below by
accessing the MicroPython REPL and running the following commands:

    >>> import upip
    >>> upip.install('micropython-logging')


[1]: https://github.com/dustin/seriesly/
[3]: https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html
[4]: https://github.com/npat-efault/picocom
[5]: http://micropython.org/webrepl/
[6]: https://www.wemos.cc/product/d1-mini-pro.html
[7]: https://www.wemos.cc/product/dht-pro-shield.html
[8]: https://www.wemos.cc/product/oled-shield.html
[9]: https://github.com/adafruit/ampy
[example_image]: https://raw.githubusercontent.com/OldhamMade/ESP8266-OLED-dht-micropython-seriesly/master/example.jpg
