from turtle import *
import colorsys
bgcolor('black')
setup(width=970, height=640)
pensize(3)
tracer(2)
h = 0

for i in range(190):
  c = colorsys.hsv_to_rgb(h, 1, 1)
  fillcolor(c)
  h += 0.996
  begin_fill()
  up()
  forward(i)
  down()
  right(9)
  forward(i)
  right(100)
  right(10)
  end_fill()
  for j in range(10):
    forward(j)
    right(83)
    backward(i)
hideturtle()
done()