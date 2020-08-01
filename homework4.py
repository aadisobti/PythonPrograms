import turtle
my_screen = turtle.getscreen()
my_turtle=turtle.Turtle()
amount = int(input ('How many squares do you want?'))
my_turtle.speed(0)
my_turtle.pencolor("red")
for x in range(amount):
  my_turtle.right(91)
  my_turtle.forward(x*5)
