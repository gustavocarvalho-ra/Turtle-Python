from turtle import * 
import colorsys
bgcolor('black')
speed(0)
pensize(3)

h = 0.0

for i in range(300):
  color = colorsys.hsv_to_rgb(h, 1, 1)
  pencolor(color)
  h += 0.005
  right(i)
  circle(50, i)
  forward(i)
  left(91)
done()