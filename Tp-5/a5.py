from turtle import *
import colorsys
bgcolor('black')
speed(0)
h = 0

for i in range(200):
  c = colorsys.hls_to_rgb(h, 1, 1)
  pencolor(c)
  h += 0.05
  circle(5 - i, 100)
  left(80)
  circle(5 - i,100)
  right(100)
  pensize(2)
done() 