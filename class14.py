"""Polygon
Outline:
Write a program to set screen size, colour for turtle graphics and draw a polygon using turtle?"""

import turtle
turtle.Screen().bgcolor("green")
turtle.Screen().setup(600,600)
polygon=turtle.Turtle()
"""polygon.forward(100)
polygon.right(90)
polygon.forward(100)
polygon.right(90)
polygon.forward(100)
polygon.right(90)
polygon.forward(100)
for i in range(4):
    polygon.forward(100)
    polygon.right(90)
polygon.penup()
polygon.goto(50,100)
polygon.pendown()
for j in range(6):
    polygon.forward(70)
    polygon.right(60)

    Star
Outline:
Write a program to draw a star using a turtle?
polygon.right(75)
polygon.forward(200)
for i in range(4):
    polygon.right(144)
    polygon.forward(200)
polygon.forward(200)
polygon.left(120)
polygon.forward(200)
polygon.left(120)
polygon.forward(200)
polygon.penup()
polygon.right(150)
polygon.forward(100)
#second triangle
polygon.pendown()
polygon.right(90)
polygon.forward(200)
polygon.right(120)
polygon.forward(200)
polygon.right(120)
polygon.forward(200)
Spiral pattern
Outline:
Write a program to draw a square inside a square?"""
size=0
while True:
    for i in range(4):
        polygon.forward(size+1)
        polygon.left(90)
        size=size-5
    size=size+1


turtle.done()