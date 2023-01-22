import turtle
import random
from turtle import TurtleScreen as screen
myS = turtle.getscreen()
t = turtle.Turtle()
t.speed(0)
t.width(5)
animals = [
    'zebra', 'cobra', 'stork', 'penguin', 'shark', 'elephant', 'buffalo',
    'whale', 'wolf', 'seal', 'eagle', 'wren', 'horse', 'rattlesnake', 'ape',
    'crow', 'tuna']
x = random.choice(animals)

print(x)
turtle.listen()


def f():
    t.setheading(90)
    t.fd(100)
turtle.onkey(f, "Up")



def d():
    t.setheading(270)
    t.fd(100)
turtle.onkey(d, "Down")


def e():
    t.setheading(180)
    t.fd(100)
turtle.onkey(e, "Left")


def g():
    t.setheading(0)
    t.fd(100)
turtle.onkey(g, "Right")


def clickRight(x, y):
    col = input("Enter the color name or hex value of color(# RRGGBB): ")
    t.fillcolor(col)
    t.begin_fill()


def x():
    t.end_fill()
turtle.onkey(x, "x")
turtle.onscreenclick(clickRight, 1)
turtle.mainloop()
