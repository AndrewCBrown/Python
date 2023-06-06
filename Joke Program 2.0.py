#Joke Program 2.0 by Andrew Brown 9/14/2018

#Greeting
print("Hello! Welcome to my introduction program, I'd like to get to know you better!")

#Ask 3 questions and get user input
gender=input("What is your gender?: ")
name=input("What is your name?: ")
print("Hey,",name,"!")
print("What is your favorite color,",name,"?: ")
color=input()
print("Oooo, good choice!")
animal=input("What is your favoite animal?:")

#Calculations
if gender in('boy', 'Boy', 'man', 'Man', 'male', 'Male', 'guy', 'Guy', 'm', 'M', 'BOY', 'MAN', 'MALE', 'GUY'):
    gen="his"
if gender in('girl', 'Girl', 'woman', 'Woman', 'female', 'Female', 'gal', 'Gal', 'f', 'F', 'GIRL', 'WOMAN', 'FEMALE', 'GAL'):
    gen="her"

#Create joke
print("One day,",name,"was going to work, wearing",gen,"favorite",color,"pants.\nThen, all of a sudden, a",animal,"jumped out of the trees and had a heart attack\nbecause of how ugly the",color,"pants were. The end.")
