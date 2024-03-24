import turtle
from turtle import *

bgcolor('black')
up()
setpos(90, 90)
down()
hideturtle()
speed(0)

def line(i):
  for c in range(i):
    forward(c)