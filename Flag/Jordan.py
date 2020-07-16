import turtle
import subprocess
#from turtle import *
import time


wn = turtle.Screen()
wn.bgcolor("maroon")
turtle = turtle.Turtle()
turtle.speed(5)
turtle.penup()
turtle.shape("turtle")

turtle.goto(-300,-300)
turtle.setheading(0)
turtle.pendown()

#-----------------------Ground---------------------

turtle.begin_fill()
turtle.color("yellow")
turtle.forward(90)
turtle.left(90)
turtle.forward(15)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(15)
turtle.back(15)
turtle.left(90)
turtle.end_fill()
turtle.forward(15)

turtle.begin_fill()
turtle.left(90)
turtle.forward(15)
turtle.right(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(15)
turtle.end_fill()

turtle.back(15)
turtle.right(90)
turtle.forward(15)
turtle.begin_fill()
turtle.right(90)
turtle.forward(15)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(15)
turtle.end_fill()

turtle.backward(15)
turtle.left(90)
turtle.forward(10)
turtle.left(90)

#-------------------Stand-----------------------

turtle.begin_fill()
turtle.color("gray")
turtle.forward(550)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(550)
turtle.end_fill()

turtle.backward(535)
turtle.left(90)

#-----------------Jordan flag 1st red part------------------

turtle.begin_fill()
turtle.color("black")
turtle.forward(250)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(250)
turtle.end_fill()

turtle.left(180)

#-----------------Jordan flag yellow part------------------

turtle.begin_fill()
turtle.color("white")
turtle.forward(250)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(250)
turtle.end_fill()

turtle.left(180)

#-----------------Jordan flag 2nd red part------------------

turtle.begin_fill()
turtle.color("green")
turtle.forward(250)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(250)
turtle.end_fill()

#-----------------Jordan flag triangle part------------------

turtle.begin_fill()
turtle.color("red")
turtle.right(150)
turtle.forward(148)
turtle.left(120)
turtle.forward(148)
turtle.end_fill()

#-----------------Jordan flag star part------------------
turtle.left(120)
turtle.forward(70)
turtle.left(90)
turtle.forward(43)


turtle.begin_fill()
turtle.color("white")
for i in range(7):
    angle = 180.0 - 180.0 / 7
    turtle.forward(18)
    turtle.right(angle)
    turtle.forward(18)
turtle.end_fill()
turtle.penup()
turtle.forward(220)
turtle.right(90)
turtle.forward(350)

turtle.color('White')
style = ('Comic Sans MS', 30, 'italic')
turtle.write('Flag of Jordan', font=style, align='center')
turtle.forward(40)
style = ('Comic Sans MS', 24)
turtle.write('Created By: Shaiful', font=style, align='center')
turtle.hideturtle()

wn.exitonclick()