from turtle import Turtle, Screen, colormode, window_width, window_height, mode, setworldcoordinates
from random import randrange
from shapes import Shapes
from random_path import Path
from spirograph import Spirograph
from painting import Painting

tim = Turtle()

tim.shape("turtle")
tim.color("cyan1")


# creating dash_lines
# for _ in range(10):
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     tim.forward(10)

# # CREATING DIFFERENT SHAPES OF TURTLE'S WALK
#
#
# tim.penup()
# tim.goto(-75, 75)
# tim.pendown()
#
#
# for i in range(3, 8, 1):
#     Shapes(i, tim).creating_lines()
#     colormode(255)
#     r = randrange(0, 255, 5)
#     g = randrange(0, 255, 5)
#     b = randrange(0, 255, 5)
#     tim.pencolor((r, g, b))


# RANDOM PATH OF TURTLE
#
# tim.speed(10)
#
# while True:
#     Path(tim).random_path()
#     Path(tim).random_thickness()
#     Path(tim).random_color()

# MAKING A SPIROGRAPH
# tim.speed("fastest")
# i = 576
#
# for _ in range(i):
#     Spirograph(tim, 100, i).circle()
#     Spirograph(tim, 100, i).random_color()

# MAKING A PAINTING
tim.speed("fastest")
my_paint = Painting(tim, 50, 20)

my_paint.set_position()
my_paint.making_dot()



screen = Screen()
screen.exitonclick()