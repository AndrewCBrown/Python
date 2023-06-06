#Arithmetic Operators Program by Andrew Brown 9/15/2018

#Greeting
print("Welcome to the arithmetic operators program!")
print("In this program you will enter two integers, one at a time,\nand it will perform all the arithmetic operations to those\ntwo integers and give the results!\n")

#User Input
a=int(input("What is the first integer?: "))
b=int(input("What is the second integer?: "))

#Calculations
Sum=a+b
Difference=a-b
Product=a*b
Quotient=a/b
Exponentiation=a**b
TruncatedDivision=a//b
Modulus=a%b

#Print Result
print(a,"+",b,"=",Sum,sep="")
print(a,"-",b,"=",Difference,sep="")
print(a,"*",b,"=",Product,sep="")
print(a,"/",b,"=",Quotient,sep="")
print(a,"^",b,"=",Exponentiation,sep="")
print(a,"//",b,"=",TruncatedDivision,' ("//" is truncated division)',sep="")
print(a,"%",b,"=",Modulus,' ("%" is modulus)',sep="")
