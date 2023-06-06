#Pi Program by Andrew Brown 9/20/2018

#Greeting
print("This program is designed to calculate Pi to 10 decimal places!\n")

#Calculations
import random
loops=100000000
i=1
inside=0
while (i<loops):
    x=(random.randint(0,10000000000))/10000000000
    y=(random.randint(0,10000000000))/10000000000
    if ((x**2+y**2)**(1/2)<=1):
        inside=inside+1
    i=i+1
pi=4*inside/loops
#Print Result
print("Pi is approximately equal to ", pi, "!",sep="")
