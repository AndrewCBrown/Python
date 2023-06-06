#Exponential Program by Andrew Brown 9/4/2018

#Greeting
print("Hello! This program allows you to do exponential calculations.")
print("First, you will enter a base number.\nNext, you will enter the power that you want to raise that base to.")
print("For example, to calculate 3^7, you will enter '3' and then '7'.")
      
#Get base number from user
print("\n\n")
base=float(input("Enter the base number to which you will raise to an exponent then press 'Enter': "))

#Get exponent number from user
exponent=float(input("Enter the exponent number that you are raising the base to then press 'Enter': "))

#Calculate answer
answer=base**exponent

#Display answer
print(base,"^",exponent,"=")
print(answer)
