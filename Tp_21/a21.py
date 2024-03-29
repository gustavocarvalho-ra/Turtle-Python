import turtle as t
import colorsys
t.bgcolor('black')
t.tracer(300)

def draw():
  h = 0
  n = 10
  for i in range(125):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h == 1/n
    t.pencolor('black')
    t.pensize(1)
    t.rt(119)
    t.circle(i, 155, steps=1)
    t.end_fill()
    t.rt(100)
    t.bk(20)
    t.circle(i, 296, steps=1)
    t.end_fill()
    for j in range(26):