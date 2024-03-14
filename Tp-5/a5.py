from turtle import *
import colorsys as cs

speed(0)
pensize(3)
bgcolor('black')
h = 0

for i in range(300):
  c = cs.hls_to_rgb(h,1,1)
  pencolor(c)
  h += 0.005
  circle(5 - i, 100)
  lt(80)
  circle(5 - i,100)
  rt(100)
done()