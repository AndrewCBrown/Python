#Integer Division Program by Andrew Brown 9/10/2018
#Greeting
print("Welcome to the division program!\nYou will enter two integers and the second number will be divided by the\nfirst and the result will be displayed to two decimal places.")
print("")

#User Input
numerator=int(input("Give an integer for the dividend and press enter:"))
denominator=int(input("Give an integer for the divisor and press enter:"))

#Calculations
answer=float(numerator/denominator)

#Display Result
print(numerator,"/",denominator,"=",format(answer,".2f"),sep="")
