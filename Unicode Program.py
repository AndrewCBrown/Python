#Unicode Program by Andrew Brown 9/15/2018

#Greeting
print("Welcome to the unicode program!\nIn this program you will be asked to enter an upper or a lowecase letter and it will produce the unicode value of that letter!\n")

#User Input
letter=input("What letter would you like to know the unicode value of?: ")

#Calculations
unicode=ord(letter)

#Print Result
print(letter,"'s unicode value is: ",unicode,sep="")
