from turtle import Turtle, Screen
from random import random,choice

tim = Turtle()
tim.color("DarkGreen")
# challenge 1
# for i in range(4):
#     tim.left(90)
#     tim.forward(100)
# # challenge 2
# for i in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
# challenge 3
# tim.penup()
# tim.setposition(0,200)
# tim.pendown()
# for times in range (7):
#     tim.pencolor(random(), random(), random(), )
#     for sides in range(times+3):
#         tim.right(360/(times+3))
#         tim.forward(200)
# challenge 4
# tim.speed(20)
# tim.pensize(10)
# angles = [90, 180, 270, 360]
# for walk in range(100):
#     tim.right(choice(angles))
#     tim.pencolor(random(), random(), random())
#     tim.forward(25)
# challenge 5
tim.speed("fastest")
tim.pensize(2)
initial_heading = tim.heading()
tim.right(5)
while initial_heading != tim.heading():
    tim.pencolor(random(), random(), random())
    tim.circle(150)
    tim.right(5)



























display = Screen()
display.exitonclick()