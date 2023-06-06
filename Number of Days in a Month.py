#Number of Days in a Month Program by Andrew Brown 9/18/2018

#Greeting
print("Welcome to the days in a month program!")
print("In this program you will be asked to enter a month and then\nit will tell you how many days are in that month!\n")

#User Input (month)
month=input("Which month would you like to know the number of days for?: ")
if (month=="febuary"):
    month="Febuary"
while month not in("Febuary", "febuary", "January", "january", "March", "march", "May", "may", "July", "july", "August", "august", "October", "october", "December", "december","April", "april", "June", "june", "September", "september", "November", "november"):
    print("You didn't enter a month or spell it correctly!")
    month=input("Which month would you like to know the number of days for?: ")
if (month=="febuary"):
    month="Febuary"
    
#If Febuary, ask year
if (month=="Febuary"):
    year=int(input("What year did you want to know this for?(enter 4 digits): "))

#Calculations
if (month in("January", "january", "March", "march", "May", "may", "July", "july", "August", "august", "October", "october", "December", "december")):
    days=31
elif (month in("April", "april", "June", "june", "September", "september", "November", "november")):
    days=30
elif ((month=="Febuary" and year%4!=0) or ((month=="Febuary") and (year in(1700, 1800, 1900, 2100)))):
    days=28
elif ((month=="Febuary") and (year%4==0)):
    days=29
else:
    print("You didn't enter a month or spell it correctly!")
    days=0
      
#Print Result
if (days>0):
    if (month=="Febuary"):
        print("In ",year," there are ",days," days in Febuary!",sep="")
    else:    
        print("There are ",days," days in ",month,"!",sep="")

    
