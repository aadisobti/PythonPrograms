

import turtle
from turtle import TurtleScreen as screen
myS=turtle.getscreen()
t=turtle.Turtle()
def f():
    t.fd(100)
screen.onkeypress(f, "Up")

def d():
    t.backward(100)
screen.onkeypress(d, "Down")


def e():
    t.left(90)
    t.fd(100)
screen.onkeypress(e, "Left")


def g():
    t.right(90)
    t.fd(100)
screen.onkeypress(g, "Right")
