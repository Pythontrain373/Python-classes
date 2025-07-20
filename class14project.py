import turtle
turtle.Screen().bgcolor("black")
turtle.Screen().setup(600,600)
square=turtle.Turtle()
for i in range(4):
    for color in ('red','blue','cyan','green'):
        square.hideturtle()
        square.color(color)
        square.forward(60)
        square.right(90)