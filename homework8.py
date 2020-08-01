import turtle
my_screen = turtle.getscreen()
t=turtle.Turtle()
t.speed(0)
colors = ["red", "yellow", "blue", "green"]
for x in range(100):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(91)
t.penup()
t.goto(150,150)
t.pendown()
for x in range(20):
    t.circle(50)
    t.right(45)
t.penup()
t.goto(-150,150)
t.pendown()
for x in range(100):
    t.forward(x)
    t.right(46)
t.penup()
t.goto(-150,-150)
t.pendown()
for x in range(25):
    t.fd(x*10)
    t.right(144)
t.penup()
t.goto(160,-160)
t.pendown()
for n in range(27):
        t.fd(n*10)
        t.right(121)
for x in range(27):
        t.fd(n*10)
        t.right(119)

