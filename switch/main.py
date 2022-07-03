"""
switch/main.py - Light switch main.py
"""
from esp import espnow
import network
from machine import Pin
import sys
import ujson

DEBUG = False

SWITCH_MAC = b'|\x87\xce\xf6\xcfd'
LIGHT_MAC = b'|\x9e\xbd0R\x08'

# espnow requires an active WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# ESP-NOW
now = espnow.ESPNow()
now.init()
now.add_peer(LIGHT_MAC)

# LED & Button
led = Pin(21, mode=Pin.OUT)
button = Pin(17)
button.init(mode=Pin.IN, pull=Pin.PULL_UP)


def setup() -> bool:
    button_value = button.value()
    led.value(
        1 if button_value else 0
    )
    return button_value


def loop():
    last_value = setup()
    while True:
        value = button.value()
        # Handle state change
        if value != last_value:
            last_value = value
            # Toggle the light on the microcontroller so the user knows
            # what the new state is
            led.value(1 if value else 0)
            # JSON-serialize the value & update the light
            payload = ujson.dumps(value)
            now.send(LIGHT_MAC, payload, True)


try:
    setup()
    loop()
except Exception as err:
    print(err)
    if not DEBUG:
        # If we're not debugging and we hit an uncaught exception
        # Just reboot, there's no way for us to recover at this point
        sys.exit()
