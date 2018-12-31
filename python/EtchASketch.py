# Etch-a-sketch using Pygame & Turtles

import turtle
from sys import exit

scr = turtle.Screen()
t = turtle.Turtle()

hasQuit = False

def up():
    t.sety(t.ycor()+10)

def down():
    t.sety(t.ycor()-10)

def left():
    t.forward(-10)

def right():
    t.forward(10)

x_shift = 0
y_shift = 0

scr.onkey(up, "Up")
scr.onkey(down, "Down")
scr.onkey(right, "Right")
scr.onkey(left, "Left")
scr.listen()

scr.mainloop()
