import threading
import time 

import turtle



window = turtle.Screen ()
a = turtle.Turtle ()
turtle = turtle.Turtle ()
turtle.speed(0)                               #speed and coulor ect. 
a.speed(0)
turtle.color ('white')
a.color ('white')


def drawasquare(a):
    for x in range (4):
         a.forward(150)    # draaw one square
         a.right(90)

def drawhex (a):
    for x in range (6):
        turtle.forward (150)           #draw a hexagon (one)
        turtle.right (60)  

def thing (wichturtule):
    for x in range (3):
        t.forward (100)
        t.right (90)

def func1 ():
    for x in range (10):
        window.bgcolor ("black")
        time.sleep(1)
        window.bgcolor ("red")
        time.sleep(1)
        window.bgcolor ("blue")
        time.sleep(1)
        window.bgcolor ("green")
        time.sleep(1)
        window.bgcolor ("yellow")
        time.sleep(1)
        window.bgcolor ("purple")
        time.sleep(1)
        

 
       


def func2() :    
    for loopCounter in range(72):
        drawasquare(turtle)
        turtle.left(5)
        
    


def func3() :    
    for loopCounter in range(72):
        drawhex (a)
        a.left(5)
       


def colortrithing (t):
    colourcounter = 1
    for loopCounter in range (72):
        drawtri

t = threading.Thread(target = func1)
t.start()

t = threading.Thread(target = func2)
t.start ()   


window.exitonclick()


