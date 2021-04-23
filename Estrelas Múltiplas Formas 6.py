from turtle import *
import turtle

a = turtle.Screen()

goto(-150, 0)
bgcolor("black")
color("yellow")
speed(0)

begin_fill()
points = 1
while points < 5:
    forward(300)
    right(145)
    points = points + 1
end_fill()

hideturtle()
a.exitonclick()