#Binary Program by Andrew Brown 9/4/2018

#Greeting
print("Welcome to my binary number program!")
print("This program will take an 8-digit binary number and convert it to base 10.")
print("You will enter the digits one at a time (pressing enter after each digit) from left to right in the sequence.")
print("For example, to get the number 3, you would enter '00000011'.")

#User Input
print("\n\n")
a=int(input("Enter the 1st digit in the sequence (either 0 or 1) then press enter: "))
b=int(input("Enter the 2nd digit in the sequence (either 0 or 1) then press enter: "))
c=int(input("Enter the 3rd digit in the sequence (either 0 or 1) then press enter: "))
d=int(input("Enter the 4th digit in the sequence (either 0 or 1) then press enter: "))
e=int(input("Enter the 5th digit in the sequence (either 0 or 1) then press enter: "))
f=int(input("Enter the 6th digit in the sequence (either 0 or 1) then press enter: "))
g=int(input("Enter the 7th digit in the sequence (either 0 or 1) then press enter: "))
h=int(input("Enter the 8th digit in the sequence (either 0 or 1) then press enter: "))

#Calculation
answer=a*128+b*64+c*32+d*16+e*8+f*4+g*2+h

#Print Answer
print(a,b,c,d,e,f,g,h,"=",answer)
