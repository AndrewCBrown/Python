#Temperature Conversion Program with functions by Andrew Brown 10/9/2018

#Greeting
print("Hello! This program converts temperature.\nYou will specify to convert from Celsius to Fahrenheit\nor vice versa, and then you will enter the temperature.")

#Define Functions
def temp_convertFC(userTemp):
    return 5/9*(userTemp-32)

def temp_convertCF(userTemp):
    return userTemp*(9/5)+32

#User Input
converter=input("Enter CF to convert from Celsius to Fahrenheit\nor enter FC to convert from Fahrenheit to Celsius: ")

#Program loop
while converter!="done":

    while converter!="FC" and converter!="CF" and converter!="done":
        converter=input("That is not a valid input!\nPlease enter 'CF' or 'FC': ")
        
    userTemp=float(input("Enter the temperature you would like to convert: "))

    if converter=="FC":
        c=temp_convertFC(userTemp)
        print("\n",userTemp,chr(186),"Fahrenheit is equal to ",c,chr(186),"Celsius!",sep="")

    elif converter=="CF":
        f=temp_convertCF(userTemp)
        print("\n",userTemp,chr(186),"Celsius is equal to ",f,chr(186),"Fahrenheit!",sep="")

    converter=input("\nEnter CF to convert from Celsius to Fahrenheit\nor enter FC to convert from Fahrenheit to Celsius\nOr enter 'done' to exit the program: ")

print("Thank you for using the converter!")
