# Overview
This repo contains code for 2 ESP32 microcontrollers.

1. Switch - The microcontroller that acts as a light switch. When a button is pressed, the light is on. When button is not pressed, the light is off.
2. Light - The microcontroller that turns an LED light on. Responds to the data received from the Switch device.

The 2 microcontrollers communicate using ESP-NOW

## Hardware
- [Adafruit ESP32 Feather Board](https://www.adafruit.com/product/3405) x 2
- [Metal On/Off Switch with Green LED](https://www.adafruit.com/product/482)
- [5MM White LEDs](https://www.adafruit.com/product/754)


## Firmware
- [Micropython w/ ESP-NOW](https://github.com/glenn20/micropython-espnow-images/blob/main/20220423_espnow-g20-v1.18-14-g78cdcdfdc)
- [ESP-NOW Docs](https://micropython-glenn20.readthedocs.io/en/latest/library/espnow.html#introduction)