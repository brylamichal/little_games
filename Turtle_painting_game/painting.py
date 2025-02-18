from turtle import window_height, window_width, mode, colormode
from random import randrange
from math import fabs
class Painting():
    def __init__(self, name, space, size_dot):
        self.name = name
        self.space = space
        self.size_dot = size_dot
    def set_position(self):
        rest_x = ( window_width() % self.space ) / 2 + self.space / 2
        rest_y = ( window_height() % self.space ) / 2 + self.space / 2

        mode("logo")

        self.name.penup()
        self.name.ht()

        x = window_width() / 2 - rest_x
        y = - window_height() / 2 + rest_y
        self.name.setposition(x, y)

        self.name.st()
        self.name.left(90)
    def making_dot(self):
        rest_x = ( window_width() % self.space ) / 2 + self.space / 2
        rest_y = ( window_height() % self.space ) / 2 + self.space / 2

        end_x = window_width() / 2 - rest_x
        end_y = window_width() / 2 - rest_y

        current_x = fabs(self.name.xcor())
        current_y = fabs(self.name.ycor())

        while end_y >= current_y:
            while end_x >= current_x:
                colormode(255)
                r = randrange(0, 255, 5)
                g = randrange(0, 255, 5)
                b = randrange(0, 255, 5)

                self.name.dot(self.size_dot, (r, g, b))
                self.name.forward(self.space)

                current_x = fabs(self.name.xcor()) + self.space

            colormode(255)
            r = randrange(0, 255, 5)
            g = randrange(0, 255, 5)
            b = randrange(0, 255, 5)

            self.name.dot(self.size_dot, (r, g, b))
            self.name.seth(0)
            self.name.forward(self.space)

            cur_x = self.name.xcor()
            if cur_x - rest_x > - window_width() / 2 + rest_x:
                self.name.left(90)
            else:
                self.name.right(90)

            current_y = fabs(self.name.ycor()) + self.space / 2
            current_x = fabs(self.name.xcor())
        self.name.ht()
