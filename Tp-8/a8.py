from turtle import *
import colorsys
bgcolor('black')
speed(0)
h = 0

for i in range (200):
  c = colorsys.hsv_to_rgb(h, 1, 1)
  h += 0.05
  pencolor(c)
  left(1000)
  penup()
  forward(1)
  pendown()
  circle(i , -90)
  right(200)
  forward(i)
  left(120)
  pendown()
  forward(7)
  left(909)
  pensize(2)
done()