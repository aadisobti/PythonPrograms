import turtle
my_screen = turtle.getscreen()
my_turtle=turtle.Turtle()
my_turtle.speed(0)
turtle.bgcolor("green")
for x in range(100):
    my_turtle.right(1)
    for x in range(5):
        my_turtle.fd(100)
        my_turtle.right(144)

