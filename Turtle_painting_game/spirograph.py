from turtle import colormode
from random import randrange

class Spirograph():
    def __init__(self, name, rad, iteration):
        self.name = name
        self.radius = rad
        self.iteration = iteration
    def random_color(self):
        colormode(255)
        r = randrange(0, 255, 5)
        g = randrange(0, 255, 5)
        b = randrange(0, 255, 5)
        self.name.pencolor((r, g, b))
    def circle(self):
        self.name.circle(self.radius)
        alpha = 360 / self.iteration
        self.name.right(alpha)
