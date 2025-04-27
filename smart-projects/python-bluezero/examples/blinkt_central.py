from time import sleep
from bluezero import blinkt
import secrets


leds = blinkt.BLE_blinkt(name='Blinkt')

leds.connect()

for x in range(10):
    sleep(0.25)
    leds.set_all(255, 0, 0)
    sleep(0.25)
    leds.clear_all()


for y in range(180):
    pix = secrets.SystemRandom().randrange(1, 8)
    red = secrets.SystemRandom().randrange(0, 255)
    green = secrets.SystemRandom().randrange(0, 255)
    blue = secrets.SystemRandom().randrange(0, 255)
    leds.clear_all()
    leds.set_pixel(pix, red, green, blue)
    sleep(0.05)

leds.set_all(255, 0, 0)
sleep(2)
leds.clear_all()
leds.disconnect()
