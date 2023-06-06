#Turtle Race program by Andrew Brown 11/12/2018

import turtle
import random

#Initialize the number of turtles
turtlesQ=10

#Set window size
turtle.setup(900,900)

#Get turtle window
window=turtle.Screen()

#Set window title
window.title("Turtle Race Track")

#Initialize screen layout parameters
start_loc=(-400,-300)
finish_line=350
track_separation=60
forward_incr=6

window.bgcolor("blue")

#Draw the finish line
Lakitu=turtle.Turtle()
Lakitu.fillcolor("white")
Lakitu.shape("circle")
Lakitu.pensize(2)
Lakitu.penup()
Lakitu.setposition(finish_line,start_loc[1])
Lakitu.left(90)
Lakitu.pendown()
Lakitu.forward(600)
Lakitu.penup()
Lakitu.turtlesize(.001,.001)

#Define the 10 turtles
turtleList=["Al","Ben","Cam","Dom","Eric","Fred","Gina","Ham","Irv","Jan"]
#Set turtle colors
colors=["dark red","red","orange","yellow","chartreuse","green","turquoise","blue","violet","purple"]


#Define functions

def generateTurtles(turtleList,colors):
    x=0
    turtles=[]
    for name in turtleList:
        name=turtle.Turtle()
        name.fillcolor(colors[x])
        turtles.append(name)
        name.penup()
        name.turtlesize(2,2)
        name.shape("turtle")
        x+=1
    return turtles
    
def placeTurtles(turtles,start_loc,track_separation):
    for i in range(turtlesQ):
        y=track_separation*i
        turtles[i].setposition(start_loc[0],start_loc[1]+y)

def startTurtles(turtles,finish_line,forward_incr):
    while True:
        for i in range(10):
            move=random.randint(0,forward_incr)
            turtles[i].forward(move*5)
            if turtles[i].xcor()>=finish_line:
                winner=i
                return turtleList[winner]

#Main
#Generate and initialize turtles
turtles=generateTurtles(turtleList,colors)

#Place turtles at starting line
placeTurtles(turtles,start_loc,track_separation)

#Start turtles
winner=startTurtles(turtles,finish_line,forward_incr)

#Victory dance for winner
for i in range(18):
    turtles[turtleList.index(winner)].right(5)
    turtles[turtleList.index(winner)].turtlesize(3,3)
    turtles[turtleList.index(winner)].right(5)
    turtles[turtleList.index(winner)].turtlesize(2.7,2.7)
    turtles[turtleList.index(winner)].right(5)
    turtles[turtleList.index(winner)].turtlesize(2.4,2.4)
    turtles[turtleList.index(winner)].right(5)
    turtles[turtleList.index(winner)].turtlesize(2.1,2.1)

#All loser turtles cry and go away    
for i in range(10):
    if turtles[i].xcor()<finish_line:
        turtles[i].left(180)
        turtles[i].turtlesize(1.8,1.8)
        turtles[i].turtlesize(1.6,1.6)
        turtles[i].turtlesize(1.4,1.4)
        turtles[i].turtlesize(1.2,1.2)
        turtles[i].turtlesize(1,1)
        turtles[i].turtlesize(.8,.8)
        turtles[i].turtlesize(.6,.6)
        turtles[i].turtlesize(.4,.4)
        turtles[i].turtlesize(.2,.2)
        turtles[i].turtlesize(.001,.001)
    
#Display winning turtle
print("The winner is "+winner+", the "+colors[turtleList.index(winner)]+" turtle!")

#Terminate program when close window
turtle.exitonclick()
