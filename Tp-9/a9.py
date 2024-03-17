import turtle
import colorsys

t = turtle.Turtle()
turtle.Screen().bgcolor('black')
t.pensize(3)
t.speed(0)
n=100
h=0

for i in range (180):
  c = colorsys.hsv_to_rgb(h, 1, 1)
  h += 1/n
  t.color(c)
  t.left(250)
  t.forward(i * 1.5)
  t.right(40)
  t.backward(i * 2)
  t.circle(60, 90)
turtle.done()