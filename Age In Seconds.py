#Age In Seconds Program by Andrew Brown 9/16/2018-9/19/2018

#Greeting
print("Welcome to the age in seconds program!")
print("In this program you will enter your birth date,\nand it will tell you how many seconds old you are!")

#User Input
birthYear=int(input("What year were you born in?(Enter 4 digits): "))
birthMonth=int(input("What month were you born in?(Enter 1 for January, 2 for Febuary, etc.): "))
birthDay=int(input("What day were you born on?: "))

#Calculations

##This block retrieves the current year, month, and day.
import datetime
now=datetime.datetime.now()
currentYear=int(now.year)
currentMonth=int(now.month)
currentDay=int(now.day)

##I divided up the user's life into 3 major sections, their first partial year, the partial of the current year, and all years in between.

###This section is to calculate the number of days the user lived in their first partial year.
####In these next 3 lines I am determining if I will need to add 1 because of the person being born before leap day on a leap year.
birthLeap=0    
if ((birthYear%4==0) and (birthYear!=1900) and (((birthMonth -1)*31 + birthDay)<=60)):
    birthLeap=1

if (birthMonth==12):
    A=31
if (birthMonth==11):
    A=61
if (birthMonth==10):
    A=92
if (birthMonth==9):
    A=122
if (birthMonth==8):
    A=153
if (birthMonth==7):
    A=184
if (birthMonth==6):
    A=214
if (birthMonth==5):
    A=245
if (birthMonth==4):
    A=275
if (birthMonth==3):
    A=306
if (birthMonth==2):
    A=334
if (birthMonth==1):
    A=365

A=A-birthDay+birthLeap
####A is now the number of days the person lived in their birth year.

###This section is to calculate the number of days the user lived in between their first year and the current year. "B" will be used to represent this quantity.
####Aside: It could be very accurate to just multiply all these middle years by 365.25 to get the days, but not exact, so I will calculate it exactly.
####This first large if statement (next 26 lines) will be for users who have lived through several leap years, for younger users I will use different methods.
if ((currentYear-birthYear)>=9):
    fullYears=(currentYear-birthYear)-1
    
    ####This block calculates how many full years the user lived before their first full leap year.
    if (birthYear%4==0):
        initFullYears=3
    if (birthYear%4==1):
        initFullYears=2
    if (birthYear%4==2):
        initFullYears=1
    if (birthYear%4==3):
        initFullYears=0
    
    ####This block calculates how many full years are between the current year and the most recent leap year.
    if (currentYear%4==0):
        endFullYears=3
    if (currentYear%4==1):
        endFullYears=0
    if (currentYear%4==2):
        endFullYears=1
    if (currentYear%4==3):
        endFullYears=2
    
    middleFullYears=fullYears-(initFullYears+endFullYears)
    B=((middleFullYears-1)*365.25)+(366)+((initFullYears+endFullYears)*365)
    ####B is now the number of days the person lived in their full years(in between their first partial year and the current partial year).

if (currentYear-birthYear==8):
    if (birthYear%4==0):
        B=(365*6)+366
    else:
        B=(365*5)+(366*2)

if (currentYear-birthYear==7):
    if (3>=birthYear%4>=2):
        B=(365*4)+(366*2)
    else:
        B=(365*5)+366

if (currentYear-birthYear==6):
    if (birthYear%4==3):
        B=(365*3)+(366*2)
    else:
        B=(365*4)+366

if (currentYear-birthYear==5):
    B=(365*3)+366

if (currentYear-birthYear==4):
    if (birthYear%4==0):
        B=365*3
    else:
        B=(365*2)+366

if (currentYear-birthYear==3):
    if (3>=birthYear%4>=2):
        B=365+366
    else:
        B=365*2

if (currentYear-birthYear==2):
    if (birthYear%4==3):
        B=366
    else:
        B=365

if (currentYear-birthYear==1):
    B=0

if (currentYear==birthYear):
    if (currentYear%4==0):
        B=-366
    else:
        B=-365
####This negative value for B will account for the fact that users born in the current year will have certain days added twice from variables A and C when the final calculation is done.

###This section is to calculate the number of days the user lived in the current year.
leapDayYet=0
if ((currentYear%4==0) and (currentMonth>=3)):
    leapDayYet=1

if (currentMonth==12):
    C=334
if (currentMonth==11):
    C=304
if (currentMonth==10):
    C=273
if (currentMonth==9):
    C=243
if (currentMonth==8):
    C=212
if (currentMonth==7):
    C=181
if (currentMonth==6):
    C=151
if (currentMonth==5):
    C=120
if (currentMonth==4):
    C=90
if (currentMonth==3):
    C=59
if (currentMonth==2):
    C=31
if (currentMonth==1):
    C=0
C=C+currentDay+leapDayYet
####C is now the number of days that have occurred so far in this current year.

secondsLived=(A+B+C)*86400


#Print Result
print("You have lived",secondsLived,"seconds!")



#I think the below 3 lines are invalid now
#if current month-2 is negtive then make the variable 0
#set a variable to be month-2
#(multiply the variable by 10 and add it to this following expression(this gets rid of errors in early march when deciding if a leap day has happened already))
