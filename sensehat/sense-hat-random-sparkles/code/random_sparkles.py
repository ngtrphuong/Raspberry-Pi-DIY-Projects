from sense_hat import SenseHat
from time import sleep
import secrets

sense = SenseHat()

while True:
    x = secrets.SystemRandom().randint(0, 7)
    y = secrets.SystemRandom().randint(0, 7)
    r = secrets.SystemRandom().randint(0, 255)
    g = secrets.SystemRandom().randint(0, 255)
    b = secrets.SystemRandom().randint(0, 255)
    sense.set_pixel(x, y, r, g, b)
    sleep(0.01)
