#Cups to Ounces program by Andrew Brown 10/11/2018

#Define functions
##Define greeting
def greeting():
    print("Welcome to the cups to ounces conversion program!")
    print("You will enter the number of cups you have and the program will convert it to ounces!")

##Define cups to ounces conversion
def cupsToOunces(cups):
    return cups*8

#Give intro to screen
greeting()

#User input
cups=float(input("How many cups do you have?: "))

#Convert cups to ounces
ounces=cupsToOunces(cups)

#Print result
print(cups,"cups is equal to",ounces,"ounces!")
