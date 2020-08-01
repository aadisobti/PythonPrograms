import turtle
my_screen = turtle.getscreen()
t=turtle.Turtle()
amount = int(input ('How many squares do you want?'))
t.speed(0)
colors = ["red", "yellow", "blue", "green"]
for x in range(amount):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(91)
