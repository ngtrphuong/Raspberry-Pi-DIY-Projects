import client as u
import secrets

u.connect()
u.clear()

while True:
    x = secrets.SystemRandom().randint(0, 7)
    y = secrets.SystemRandom().randint(0, 7)
    r = secrets.SystemRandom().randint(0, 255)
    g = secrets.SystemRandom().randint(0, 255)
    b = secrets.SystemRandom().randint(0, 255)
    u.set_pixel(x, y, r, g, b)
    u.show()
