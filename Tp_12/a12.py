import turtle
from turtle import *

turtle.title('rainbow')
speed(5)
bgcolor('black')
r,g,b = 255, 0, 0

for i in range(255*2):
  colormode(255)
  if i <255//3:
    g+=3
  elif i <255*2//3:
    r-=3