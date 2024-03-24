import turtle
t = turtle.Pen()
turtle.bgcolor('black')
colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange']

for i in range(210):
  t.pencolor(colors[i%6])
  t.width(i/100+1)
  t.forward(i)
  t.left(59)
turtle.done()