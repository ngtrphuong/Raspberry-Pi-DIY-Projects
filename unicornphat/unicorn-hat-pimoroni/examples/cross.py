#!/usr/bin/env python

import time

import unicornhat as unicorn
import secrets


print("""Cross

You should see randomly coloured dots crossing paths with each other.

If you're using a Unicorn HAT and only half the screen lights up, 
edit this example and  change 'unicorn.AUTO' to 'unicorn.HAT' below.
""")

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

points = []


class LightPoint:

    def __init__(self):

        self.direction = secrets.SystemRandom().randint(1, 4)
        if self.direction == 1:
            self.x = secrets.SystemRandom().randint(0, width - 1)
            self.y = 0
        elif self.direction == 2:
            self.x = 0
            self.y = secrets.SystemRandom().randint(0, height - 1)
        elif self.direction == 3:
            self.x = secrets.SystemRandom().randint(0, width - 1)
            self.y = height - 1
        else:
            self.x = width - 1
            self.y = secrets.SystemRandom().randint(0, height - 1)

        self.colour = []
        for i in range(0, 3):
            self.colour.append(secrets.SystemRandom().randint(100, 255))


def update_positions():

    for point in points:
        if point.direction == 1:
            point.y += 1
            if point.y > height - 1:
                points.remove(point)
        elif point.direction == 2:
            point.x += 1
            if point.x > width - 1:
                points.remove(point)
        elif point.direction == 3:
            point.y -= 1
            if point.y < 0:
                points.remove(point)
        else:
            point.x -= 1
            if point.x < 0:
                points.remove(point)


def plot_points():

    unicorn.clear()
    for point in points:
        unicorn.set_pixel(point.x, point.y, point.colour[0], point.colour[1], point.colour[2])
    unicorn.show()


while True:

    if len(points) < 10 and secrets.SystemRandom().randint(0, 5) > 1:
        points.append(LightPoint())
    plot_points()
    update_positions()
    time.sleep(0.03)
