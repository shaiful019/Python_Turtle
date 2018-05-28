import turtle
import subprocess
#from turtle import *
import time


wn = turtle.Screen()
wn.bgcolor("black")
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

#-------------------BD Flag green part------------------------

turtle.begin_fill()
turtle.color("green")
turtle.forward(300)
turtle.right(90)
turtle.forward(165)
turtle.right(90)
turtle.forward(300)
turtle.end_fill()


turtle.right(90)
turtle.forward(32.5)
turtle.right(90)
turtle.forward(140)

#----------------BD flag circle part-----------------------

turtle.begin_fill()
turtle.color("red")
turtle.circle(50)
turtle.end_fill()
turtle.end_fill()
turtle.penup()

turtle.right(90)
turtle.forward(47.5)
turtle.right(90)
turtle.forward(140)
turtle.right(180)

#-----------------Brazil flag green part------------------

turtle.begin_fill()
turtle.color("green")
turtle.forward(250)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(250)
turtle.end_fill()

turtle.right(90)
turtle.forward(75)
turtle.right(90)
turtle.forward(80)
#-----------------Brazil flag yellow part------------------

turtle.begin_fill()
turtle.color("yellow")
turtle.pendown()
turtle.right(35)
turtle.forward(60)
turtle.left(70)
turtle.forward(60)
turtle.left(110)
turtle.forward(60)
turtle.penup()
turtle.end_fill()

turtle.left(124)
turtle.forward(50)

#---------------------------Brazil flag blue part--------------------
turtle.begin_fill()
turtle.color("blue")
turtle.pendown()
turtle.left(90)
turtle.circle(15)
turtle.penup()
turtle.end_fill()

turtle.backward(15)
turtle.left(90)
turtle.forward(10)

#---------------------------Brazil flag white part--------------------

turtle.begin_fill()
turtle.color("white")
turtle.pendown()
turtle.right(40)
turtle.forward(10)
turtle.right(40)
turtle.forward(15)
turtle.right(40)
turtle.forward(10)
turtle.penup()
turtle.end_fill()

#---------------------------Brazil flag star part--------------------

turtle.right(110)
turtle.forward(5)

turtle.begin_fill()
turtle.color("white")
turtle.pendown()
turtle.circle(1)
turtle.penup()
turtle.end_fill()

turtle.forward(8)

turtle.begin_fill()
turtle.color("white")
turtle.pendown()
turtle.circle(1)
turtle.penup()
turtle.end_fill()

turtle.right(20)
turtle.forward(8)

turtle.begin_fill()
turtle.color("white")
turtle.pendown()
turtle.circle(1)
turtle.penup()
turtle.end_fill()

turtle.right(130)
turtle.forward(5)

turtle.begin_fill()
turtle.color("white")
turtle.pendown()
turtle.circle(1)
turtle.penup()
turtle.end_fill()

turtle.right(50)
turtle.forward(200)


time.sleep(10)
