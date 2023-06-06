import math
import turtle

window=turtle.Screen()
window.bgcolor("blue")

Fox=turtle.Turtle()
Fox.pensize(4)
Fox.penup()
Fox.shape("square")
Fox.turtlesize(1,1)

Fox.forward(100)
Fox.left(90)
Fox.pendown()

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

Fox.turtlesize(.0002,.0002)

##################################F000000000000000000X

F0x=turtle.Turtle()
F0x.pensize(4)
F0x.penup()
F0x.shape("square")
F0x.turtlesize(1,1)

F0x.forward(90)
F0x.left(90)
F0x.pendown()

F0x.speed(100)
a=0
hT=0
wT=0
for n in range(50):
    a=(math.pi/100)*(n+1)
    h=math.sin(a)-hT
    hT=hT+h
    w=1-math.cos(a)-wT
    wT=wT+w
    F0x.forward(90*h)
    F0x.left(90)
    F0x.forward(90*w)
    F0x.right(90)

a=0
hT=0
wT=0
F0x.left(90)
for n in range(50):
    a=(math.pi/100)*(n+1)+math.pi/2
    h=1-math.sin(a)-hT
    hT=hT+h
    w=-math.cos(a)-wT
    wT=wT+w
    F0x.forward(90*w)
    F0x.left(90)
    F0x.forward(90*h)
    F0x.right(90)

a=0
hT=0
wT=0
F0x.left(90)
for n in range(50):
    a=math.pi/100*(n-1)+math.pi
    h=-math.sin(a)-hT
    hT=hT+h
    w=1+math.cos(a)-wT
    wT=wT+w
    F0x.forward(90*h)
    F0x.left(90)
    F0x.forward(90*w)
    F0x.right(90)

a=0
hT=0
wT=0
F0x.left(90)
for n in range(50):
    a=math.pi/100*(n-1)+(3*math.pi)/2
    h=1+math.sin(a)-hT
    hT=hT+h
    w=math.cos(a)-wT
    wT=wT+w
    F0x.forward(90*w)
    F0x.left(90)
    F0x.forward(90*h)
    F0x.right(90)

F0x.turtlesize(.0002,.0002)

turtle.exitonclick()
