from turtle import *
import colorsys

speed(0)
pensize(3)
bgcolor('black')
hue = 3

for i in range(300):
  col = colorsys.hls_to_rgb(hue, 1, 1)
  pencolor(col)
  hue += 0.005
  circle(5 - i, 100)
  lt(80)
  circle(5 - i,100)
  rt(100)
done()