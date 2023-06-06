#Gender Program by Andrew Brown 9/14/2018

#Greeting
print("Welcome to the gender program!\nThis program is able to mark your gender even with different inputs!")
print("")

#User Input
gender=input("What is your gender?:")

#Calculations
if gender in('boy', 'Boy', 'man', 'Man', 'male', 'Male', 'guy', 'Guy', 'm', 'M', 'BOY', 'MAN', 'MALE', 'GUY'):
    gen='Male'
if gender in('girl', 'Girl', 'woman', 'Woman', 'female', 'Female', 'gal', 'Gal', 'f', 'F', 'GIRL', 'WOMAN', 'FEMALE', 'GAL'):
    gen='Female'

#Print Gender
print(gen)
