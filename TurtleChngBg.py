import turtle
import random
my_screen=turtle.getscreen()
t=turtle.Turtle()
t.shapesize(10,25,10)
turtle.bgcolor("blue")
t.color("dark red")
for x in range(8):
    t.goto(0,0)
    t.left(45)
    for x in range(20):
        t.circle(50)
        t.fd(25)
        R = random.random()
        B = random.random()
        G = random.random()
        t.color(R,B,G)





