import turtle
t = turtle.Turtle()

t.color('red')
t.speed(300)
t.fillcolor('green')
t.pencolor('black')

for i in range(200):
  t.begin_fill()
  t.forward(300 - i)
  t.left(170)
  t.forward(300 - i)
  t.end_fill()
