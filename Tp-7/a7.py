from turtle import *
import colorsys as cs
bgcolor('black')
speed(1000)
pensize(1)
h = 0
for i in range(200):
  c=cs.hsv_to_rgb(h,1,1)
  color(c)
  h+=0.008
  begin_fill()
  fillcolor('black')
  goto(0,0)
  forward(i)
  circle(i,-130)
  left(180)
  left(222)
  end_fill()
  left(80)
done()