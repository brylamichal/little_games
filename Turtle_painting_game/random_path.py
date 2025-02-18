from random import randrange
from turtle import colormode

class Path():
    def __init__(self, name):
        self.name = name
    def random_path(self):
        angle = randrange(0, 180, 90)
        length = 10
        self.name.right(angle)
        self.name.forward(length)
    def random_thickness(self):
        self.name.width(5)
    def random_color(self):
        colormode(255)
        r = randrange(0, 255, 5)
        g = randrange(0, 255, 5)
        b = randrange(0, 255, 5)
        self.name.pencolor((r, g, b))
