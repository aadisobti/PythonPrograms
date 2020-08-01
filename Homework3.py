import turtle
my_screen = turtle.getscreen()
my_turtle=turtle.Turtle()
amount = int(input ('How many circles do you want on each side?'))
my_turtle.speed(0)
for x in range(4):
    for x in range(amount):
        my_turtle.left(1)
        my_turtle.circle(x*1)
