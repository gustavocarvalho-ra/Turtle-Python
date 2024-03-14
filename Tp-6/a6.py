from turtle import *
import colorsys as cs
bgcolor('black')
speed(0)
pensize(3)
h = 0
for i in range (300):
  c=cs.hsv_to_rgb(h,1,1)
  pencolor(c)
  h+=0.05
  right(i)
  circle(50,i)
  forward(i)
  left(91)
done()