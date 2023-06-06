#My first turtle program by Andrew Brown 10/30/2018

import math
import turtle
turtle.setup(300,300)
window=turtle.Screen()
window.bgcolor("blue")
window.title("Foxes and Turtles")


Terry=turtle.Turtle()
Fox=turtle.Turtle()
Terri=turtle.Turtle()

Fox.pensize(4)
Fox.penup()
Fox.shape("square")
Fox.turtlesize(2,2)

Terry.pensize(3)
Terry.penup()
Terry.shape("turtle")
Terry.turtlesize(2,2)
Terry.fillcolor("orange")

Terri.pensize(3)
Terri.penup()
Terri.shape("turtle")
Terri.turtlesize(2,2)
Terri.fillcolor("white")

Fox.forward(100)
Fox.left(90)
Fox.pendown()
Terry.forward(350)
Terry.pendown()

Fox.speed(100)
a=0
hT=0
wT=0
for n in range(50):
    a=(math.pi/100)*(n+1)
    h=math.sin(a)-hT
    hT=hT+h
    w=1-math.cos(a)-wT
    wT=wT+w
    Fox.forward(100*h)
    Fox.left(90)
    Fox.forward(100*w)
    Fox.right(90)

a=0
hT=0
wT=0
Fox.left(90)
for n in range(50):
    a=(math.pi/100)*(n+1)+math.pi/2
    h=1-math.sin(a)-hT
    hT=hT+h
    w=-math.cos(a)-wT
    wT=wT+w
    Fox.forward(100*w)
    Fox.left(90)
    Fox.forward(100*h)
    Fox.right(90)

a=0
hT=0
wT=0
Fox.left(90)
for n in range(50):
    a=math.pi/100*(n-1)+math.pi
    h=-math.sin(a)-hT
    hT=hT+h
    w=1+math.cos(a)-wT
    wT=wT+w
    Fox.forward(100*h)
    Fox.left(90)
    Fox.forward(100*w)
    Fox.right(90)

a=0
hT=0
wT=0
Fox.left(90)
for n in range(50):
    a=math.pi/100*(n-1)+(3*math.pi)/2
    h=1+math.sin(a)-hT
    hT=hT+h
    w=math.cos(a)-wT
    wT=wT+w
    Fox.forward(100*w)
    Fox.left(90)
    Fox.forward(100*h)
    Fox.right(90)

Terry.speed(100)
for n in range(12):
    Terry.left(150)
    Terry.forward(200)

turtle.exitonclick()
