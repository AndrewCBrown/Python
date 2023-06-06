#Word Download Program by Andrew Brown 9/15/2018

#Greeting
print("Welcome to the word download program!")
print("In this program you will be asked to enter your internet\nconnection speed (in millions of bits per second, mbps),\nand then the program will tell you how long it would take\nto download all instances of every word ever spoken!\n")

#User Input
speed=float(input("What is your connection speed in mbps?: "))

#Calculations
seconds=5/(speed/1000000000000)

#Comment:Below I am assuming a year to be 365.25 days in order to account for leap years
yrs=seconds//31557600
partialYr=seconds%31557600

days=partialYr//86400
partialDay=partialYr%86400

hrs=partialDay//3600
partialHr=partialDay%3600

mins=partialHr//60
partialMin=partialHr%60

secs=partialMin

#Print Result
print("It would take",format(yrs,".0f"),"years,",format(days,".0f"),"days,",format(hrs,".0f"),"hours,",format(mins,".0f"),"minutes, and",secs,"seconds to download all the instances of every word ever spoken!")
