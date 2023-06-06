#Use two methods to find the area under sin(x) from 0 to 1 by monte carlo method and by midpoint method.

import math
import random
import time

#Define Functions

##Greeting
def Greeting():
    print("Welcome to the integration program!")
    print("This program will ask for the number of times it should run and\nthen it will integrate Sin(x) from 0 to 1 using two different methods.")
    print("The more times the program is run the more accurate it will be.\n")

##Steps
def getSteps():
    steps=input("How many times would you like the calculation to run?: ")
    while not (steps.isdigit() and int(steps)>0):
        steps=input("That is not valid!\nPlease enter a positive integer: ")
    steps=int(steps)
    return steps

##Monte Carlo method
def MonteCarlo(steps):
    i=0
    result=0
    while i<steps:
        x=random.randint(0,1000000)/1000000.0
        y=random.randint(0,1000000)/1000000.0
        i=i+1
        if (y<=math.sin(x)):
            result=result+1/steps
    return result

##Standard Integration Method
def StandardIntegration(steps):
    function=[]
    integral=0
    for i in range(steps+1):
        x=i/steps
        function.append(math.sin(x))
    for i in range(steps):
        integral+=((function[i]+function[i+1])/2)*(1/steps)
    result=integral
    return result


#Main
Greeting()

steps=getSteps()

start_time=time.time()
Result_1=MonteCarlo(steps)
MC_time=time.time()-start_time

start_time=time.time()
Result_2=StandardIntegration(steps)
SI_time=time.time()-start_time

#Print result
print("\nThe integral from 0 to 1 of sin(x) via the Monte Carlo method\nwith",steps,"'dice rolls' is",Result_1)
print("\nThe integral from 0 to 1 of sin(x) via the standard integration method\nwith",steps,"intervals is",Result_2)
print("\nWhen ",steps," steps were used, the Monte Carlo method took ",format(MC_time,".2f")," seconds\nand the standard integration method took ",format(SI_time,".2f")," seconds.",sep="")

#These were my results for 10, 100, 10,000, and 1,000,000.
#With 10 steps I got .4 on MC and .4593145488579764 on SI
#With 100 steps I got .4300000000000002 on MC and .45969386331135786 on SI
#With 10,000 steps I got .4593999999999657 on MC and .45969769374877895
#With 1,000,000 steps I got .46040099999459994 on MC and .4596976941318224 on SI
#Standard integration is faster than montecarlo and the gap in speed increases as you use more steps

#The actual answer is 0.4596976941
