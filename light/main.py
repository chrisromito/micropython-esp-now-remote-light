"""
light/main.py - Light main.py - Turns the LED on when we receive "1"
    from the switch microcontroller
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

now = espnow.ESPNow()
now.init()

now.add_peer(SWITCH_MAC)

led = Pin(21, mode=Pin.OUT)


def loop():
    host, msg = now.irecv()
    if msg:
        value = parse_message(msg)
        led.value(value)


def parse_message(msg) -> int:
    if not isinstance(msg, str):
        msg = msg.decode()
    payload = ujson.loads(msg)
    return 1 if '1' in payload else 0


try:
    loop()
except Exception as err:
    print(err)
    if not DEBUG:
        # If we're not debugging and we hit an uncaught exception
        # Just reboot, there's no way for us to recover at this point
        sys.exit()
