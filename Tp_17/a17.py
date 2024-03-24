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
    
for i in range(200):
  width(3)
  color('red')
  left(0)
  forward(5)
  circle(i)
  width(3)
  right(45)
  color('orange')
  forward(2)
  circle(i)
  
done()