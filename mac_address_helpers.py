import network
import ubinascii

mac_as_bytes = network.WLAN().config('mac')
human_readable = ubinascii.hexlify(mac_as_bytes,':').decode()
