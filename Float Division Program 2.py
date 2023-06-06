#Float Division Program 2 by Andrew Brown 9/10/2018
#Greeting
print("Welcome to the division program!\nYou will enter two numbers and the second number will be divided by\nthe first and the result will be displayed to six decimal\nplaces in scientific notation.")
print("")

#User Input
numerator=float(input("Give a number for the dividend and press enter:"))
denominator=float(input("Give a number for the divisor and press enter:"))

#Calculations
answer=float(numerator/denominator)

#Display Result
print(format(format(answer,".6e"),"-^50"))



