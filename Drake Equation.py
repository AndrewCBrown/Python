#Drake Equation Program by Andrew Brown 8/30/2018

#Greeting
print("This is the Drake Equation Program")
print("You will enter 3 different values and then the program will give an answer")

#Defined Quantities
R=7
p=.4
n=2
f=.13

#User Input
i=int(input("1. % of life bearing planets that develop intelligent life (0-100)"))
C=int(input("2. % of intelligent civilization that can communicate with other planets(0-100)"))
L=int(input("3. The expected lifetime of such civilizations (in years)"))

#Calculate N
N=R*p*n*f*i/100*C/100*L

#Display N
print("The number of alien civilizations in our galaxy with which you can currently communicate is:")
print(N)
