import turtle
my_screen = turtle.getscreen()
my_turtle=turtle.Turtle()
amount = int(input ('How many squares do you want?'))
my_turtle.penup()
my_turtle.goto(150,150)
my_turtle.pendown()
for x in range(amount):
  my_turtle.right(91)
  my_turtle.forward(500)
