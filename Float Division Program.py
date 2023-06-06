#Float Division Program by Andrew Brown 9/10/2018
#Greeting
print("Welcome to the division program!\nYou will enter two numbers and the second number will be divided by the\nfirst and the result will be displayed to six decimal places.")
print("")

#User Input
numerator=float(input("Give a number for the dividend and press enter:"))
denominator=float(input("Give a number for the divisor and press enter:"))

#Calculations
answer=float(numerator/denominator)

#Display Result
print(numerator,"/",denominator,"=",format(answer,".6f"),sep="")
