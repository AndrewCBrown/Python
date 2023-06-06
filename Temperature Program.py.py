#Temperature Conversion Program by Andrew Brown 9/11/2018

#Greeting
print("Welcome to the temperature conversion program!")
print("Just enter the temperature in fahrenheit and it will be converted to celsius!")
print("")

#User gives Fahrenheit
fahrenheit=float(input("What is the temperature in fahrenheit?:"))

#Calculations
celsius=5/9*(fahrenheit-32)

#Print Answer
print(fahrenheit,"degrees fahrenheit is",format(celsius,".1f"),"degrees celsius.")
