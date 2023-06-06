#BMI Calculator

#Convert to metric function
def convert(height,weight):
    h=height*(0.0254)
    w=weight*(0.453592)
    return h, w

#Classify the user's BMI
def classify(BMI):
    BMI=format(BMI,".0f")
    BMI=int(BMI)
    if BMI<=18:
        Class="Underweight"
    elif 19<=BMI<=24:
        Class="Healthy"
    elif 25<=BMI<=29:
        Class="Overweight"
    elif 30<=BMI<=39:
        Class="Obese"
    elif 40<=BMI:
        Class="Extremely Obese"
    return Class

#Greeting
print("This program will give you your BMI after you enter your height and weight!")

height=float(input("What is your height in inches?: "))
weight=float(input("What is your weight in pounds?: "))

#Convert to metric
h, w =convert(height,weight)

BMI=w/(h**2)
        
Class=classify(BMI)

#Print result
print("Your BMI is ",format(BMI,".1f"),"!\nYou are ",Class,"!",sep="")
