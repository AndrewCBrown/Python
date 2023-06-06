#Coin Change Program by Andrew Brown 9/20/2018

#Greeting
print("Welcome to the make correct change game!")

#Define Target
import random
target=random.randint(1,99)
print("Make change for",target,"cents!")

#Loop (Sum<Target)
##Get coin value
##Sum coin values
Sum=0
while (Sum<target):
    coinValue=int(input("Chose a coin value (1, 5, 10, or 25)"))
    while (coinValue not in(1, 5, 10, 25)):
        print("That is not a valid coin! Try again.")
        coinValue=int(input("Chose a coin value (1, 5, 10, or 25)"))
    Sum=coinValue+Sum

#If Sum==Target, Print Congrats!
#Else Print Wrong Change!
if (Sum==target):
    print("You got it right! Congratulations!")
else:
    print("You got it wrong!")
