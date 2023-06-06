#Turtle shapes
import Stack
import turtle
import time

turtle.setup(300,300)
window=turtle.Screen()
window.bgcolor("blue")

a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0
k=0
l=0
m=0
n=0
o=0

turtles=Stack.getStack()
I=15
for names in (a, b, c, d, e, f, g, h, i, j, k, l, m, n, o):
    names=turtle.Turtle()
    names.shape("circle")
    names.fillcolor("blue")
    names.turtlesize(I,I)
    Stack.push(turtles,names)
    time.sleep(.4)
    I-=1

newturtles=Stack.getStack()
while not Stack.isEmpty(turtles):
    x=Stack.pop(turtles)
    x.hideturtle()
    time.sleep(.4)
    Stack.push(newturtles,x)


while not Stack.isEmpty(newturtles):
    x=Stack.pop(newturtles)
    x.showturtle()
    time.sleep(.4)
    Stack.push(turtles,x)

turtle.exitonclick()
