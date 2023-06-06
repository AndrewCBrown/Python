#Hayden North, Sebastian Negrete, and Andrew Brown
#10-2-18
#Calendar Program

#Greeting
print ("Hello, Welcome to this Calendar program!")
print ("This program will ask for a year and a month\nand then print out the calendar for it!\n")

#User Input
year = int(input("Enter the year you want for your calendar: "))

#Defining Valid Years
valid_years=[]
x=1799
while x<2099:
    x=x+1
    valid_years.append(x)

#Checking for a valid entry
while year not in valid_years:
    print("This program only works for years from 1800 to 2099!\nPlease enter a different year.")
    year = int(input("Enter the year you want for your calendar: "))

month = str(input("Enter the month you want for your calendar: "))
while month not in("January","February","March","April","May","June","July","August","September","October","November","December"):
    print("That is not a month!\nHint:Try entering the full name of the month with the first letter capitalized\nFor example, 'November'.")
    month = str(input("Enter the month you want for your calendar: "))
print("")

#Days in a month  
if month in ("January","March","May","July","August","October","December"):
           days = 31
    
elif month in ("April,June,September,November"):
           days = 30

elif month==("February"):
    if year%4==0:
           days = 29
    else:
           days = 28

#Calculations for what day of the week the first of the month falls on
century_digits = year//100
year_digits = year - century_digits*100
value = year_digits + year_digits//4 + 1

if (century_digits == 18 ):
    value = value + 2
elif (century_digits == 20):
    value = value + 6

if month == "January" and year%4 != 0:
    value = value + 1
elif month == "February" and year%4 != 0:
    value = value + 4
elif month == "February" and year%4 == 0:
    value = value + 3
elif month in ("March", "November"):
    value = value + 4
elif month == "May":
    value = value + 2
elif month == "June":
    value = value + 5
elif month == "August":
    value = value + 3
elif month == "October":
    value = value + 1
elif month in ("September", "December"):
    value = value + 6
 
value = value%7

#Printing one of the 28 possible calendars depending on what day of the week the first of the month is on and how many days are in the month.
if value == 1 and days == 31:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('01',' ^4'), format('02', ' ^3'), format('03', ' ^3'), format('04',' ^3'), format('05',' ^3'), format('06',' ^3'), format('07',' ^3'), '-' , sep='')
    print('-', format('08',' ^4'), format('09', ' ^3'), format('10', ' ^3'), format('11',' ^3'), format('12',' ^3'), format('13',' ^3'), format('14',' ^3'), '-' , sep='')
    print('-', format('15',' ^4'), format('16', ' ^3'), format('17', ' ^3'), format('18',' ^3'), format('19',' ^3'), format('20',' ^3'), format('21',' ^3'), '-' , sep='')
    print('-', format('22',' ^4'), format('23', ' ^3'), format('24', ' ^3'), format('25',' ^3'), format('26',' ^3'), format('27',' ^3'), format('28',' ^3'), '-' , sep='')
    print('-', format('29',' ^4'), format('30', ' ^3'), format('31', ' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 1 and days == 30:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('01',' ^4'), format('02', ' ^3'), format('03', ' ^3'), format('04',' ^3'), format('05',' ^3'), format('06',' ^3'), format('07',' ^3'), '-' , sep='')
    print('-', format('08',' ^4'), format('09', ' ^3'), format('10', ' ^3'), format('11',' ^3'), format('12',' ^3'), format('13',' ^3'), format('14',' ^3'), '-' , sep='')
    print('-', format('15',' ^4'), format('16', ' ^3'), format('17', ' ^3'), format('18',' ^3'), format('19',' ^3'), format('20',' ^3'), format('21',' ^3'), '-' , sep='')
    print('-', format('22',' ^4'), format('23', ' ^3'), format('24', ' ^3'), format('25',' ^3'), format('26',' ^3'), format('27',' ^3'), format('28',' ^3'), '-' , sep='')
    print('-', format('29',' ^4'), format('30', ' ^3'), format('', ' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 1 and days == 29:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('01',' ^4'), format('02', ' ^3'), format('03', ' ^3'), format('04',' ^3'), format('05',' ^3'), format('06',' ^3'), format('07',' ^3'), '-' , sep='')
    print('-', format('08',' ^4'), format('09', ' ^3'), format('10', ' ^3'), format('11',' ^3'), format('12',' ^3'), format('13',' ^3'), format('14',' ^3'), '-' , sep='')
    print('-', format('15',' ^4'), format('16', ' ^3'), format('17', ' ^3'), format('18',' ^3'), format('19',' ^3'), format('20',' ^3'), format('21',' ^3'), '-' , sep='')
    print('-', format('22',' ^4'), format('23', ' ^3'), format('24', ' ^3'), format('25',' ^3'), format('26',' ^3'), format('27',' ^3'), format('28',' ^3'), '-' , sep='')
    print('-', format('29',' ^4'), format('', ' ^3'), format('', ' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 1 and days == 28:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('01',' ^4'), format('02', ' ^3'), format('03', ' ^3'), format('04',' ^3'), format('05',' ^3'), format('06',' ^3'), format('07',' ^3'), '-' , sep='')
    print('-', format('08',' ^4'), format('09', ' ^3'), format('10', ' ^3'), format('11',' ^3'), format('12',' ^3'), format('13',' ^3'), format('14',' ^3'), '-' , sep='')
    print('-', format('15',' ^4'), format('16', ' ^3'), format('17', ' ^3'), format('18',' ^3'), format('19',' ^3'), format('20',' ^3'), format('21',' ^3'), '-' , sep='')
    print('-', format('22',' ^4'), format('23', ' ^3'), format('24', ' ^3'), format('25',' ^3'), format('26',' ^3'), format('27',' ^3'), format('28',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 2 and days == 31:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('',' ^4'), format('01', ' ^3'), format('02', ' ^3'), format('03',' ^3'), format('04',' ^3'), format('05',' ^3'), format('06',' ^3'), '-' , sep='')
    print('-', format('07',' ^4'), format('08', ' ^3'), format('09', ' ^3'), format('10',' ^3'), format('11',' ^3'), format('12',' ^3'), format('13',' ^3'), '-' , sep='')
    print('-', format('14',' ^4'), format('15', ' ^3'), format('16', ' ^3'), format('17',' ^3'), format('18',' ^3'), format('19',' ^3'), format('20',' ^3'), '-' , sep='')
    print('-', format('21',' ^4'), format('22', ' ^3'), format('23', ' ^3'), format('24',' ^3'), format('25',' ^3'), format('26',' ^3'), format('27',' ^3'), '-' , sep='')
    print('-', format('28',' ^4'), format('29', ' ^3'), format('30', ' ^3'), format('31',' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 2 and days == 30:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('',' ^4'), format('01', ' ^3'), format('02', ' ^3'), format('03',' ^3'), format('04',' ^3'), format('05',' ^3'), format('06',' ^3'), '-' , sep='')
    print('-', format('07',' ^4'), format('08', ' ^3'), format('09', ' ^3'), format('10',' ^3'), format('11',' ^3'), format('12',' ^3'), format('13',' ^3'), '-' , sep='')
    print('-', format('14',' ^4'), format('15', ' ^3'), format('16', ' ^3'), format('17',' ^3'), format('18',' ^3'), format('19',' ^3'), format('20',' ^3'), '-' , sep='')
    print('-', format('21',' ^4'), format('22', ' ^3'), format('23', ' ^3'), format('24',' ^3'), format('25',' ^3'), format('26',' ^3'), format('27',' ^3'), '-' , sep='')
    print('-', format('28',' ^4'), format('29', ' ^3'), format('30', ' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 2 and days == 29:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('',' ^4'), format('01', ' ^3'), format('02', ' ^3'), format('03',' ^3'), format('04',' ^3'), format('05',' ^3'), format('06',' ^3'), '-' , sep='')
    print('-', format('07',' ^4'), format('08', ' ^3'), format('09', ' ^3'), format('10',' ^3'), format('11',' ^3'), format('12',' ^3'), format('13',' ^3'), '-' , sep='')
    print('-', format('14',' ^4'), format('15', ' ^3'), format('16', ' ^3'), format('17',' ^3'), format('18',' ^3'), format('19',' ^3'), format('20',' ^3'), '-' , sep='')
    print('-', format('21',' ^4'), format('22', ' ^3'), format('23', ' ^3'), format('24',' ^3'), format('25',' ^3'), format('26',' ^3'), format('27',' ^3'), '-' , sep='')
    print('-', format('28',' ^4'), format('29', ' ^3'), format('', ' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 2 and days == 28:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('',' ^4'), format('01', ' ^3'), format('02', ' ^3'), format('03',' ^3'), format('04',' ^3'), format('05',' ^3'), format('06',' ^3'), '-' , sep='')
    print('-', format('07',' ^4'), format('08', ' ^3'), format('09', ' ^3'), format('10',' ^3'), format('11',' ^3'), format('12',' ^3'), format('13',' ^3'), '-' , sep='')
    print('-', format('14',' ^4'), format('15', ' ^3'), format('16', ' ^3'), format('17',' ^3'), format('18',' ^3'), format('19',' ^3'), format('20',' ^3'), '-' , sep='')
    print('-', format('21',' ^4'), format('22', ' ^3'), format('23', ' ^3'), format('24',' ^3'), format('25',' ^3'), format('26',' ^3'), format('27',' ^3'), '-' , sep='')
    print('-', format('28',' ^4'), format('', ' ^3'), format('', ' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 3 and days == 31:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('',' ^4'), format('', ' ^3'), format('01', ' ^3'), format('02',' ^3'), format('03',' ^3'), format('04',' ^3'), format('05',' ^3'), '-' , sep='')
    print('-', format('06',' ^4'), format('07', ' ^3'), format('08', ' ^3'), format('09',' ^3'), format('10',' ^3'), format('11',' ^3'), format('12',' ^3'), '-' , sep='')
    print('-', format('13',' ^4'), format('14', ' ^3'), format('15', ' ^3'), format('16',' ^3'), format('17',' ^3'), format('18',' ^3'), format('19',' ^3'), '-' , sep='')
    print('-', format('20',' ^4'), format('21', ' ^3'), format('22', ' ^3'), format('23',' ^3'), format('24',' ^3'), format('25',' ^3'), format('26',' ^3'), '-' , sep='')
    print('-', format('27',' ^4'), format('28', ' ^3'), format('29', ' ^3'), format('30',' ^3'), format('31',' ^3'), format('',' ^3'), format('',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 3 and days == 30:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('',' ^4'), format('', ' ^3'), format('01', ' ^3'), format('02',' ^3'), format('03',' ^3'), format('04',' ^3'), format('05',' ^3'), '-' , sep='')
    print('-', format('06',' ^4'), format('07', ' ^3'), format('08', ' ^3'), format('09',' ^3'), format('10',' ^3'), format('11',' ^3'), format('12',' ^3'), '-' , sep='')
    print('-', format('13',' ^4'), format('14', ' ^3'), format('15', ' ^3'), format('16',' ^3'), format('17',' ^3'), format('18',' ^3'), format('19',' ^3'), '-' , sep='')
    print('-', format('20',' ^4'), format('21', ' ^3'), format('22', ' ^3'), format('23',' ^3'), format('24',' ^3'), format('25',' ^3'), format('26',' ^3'), '-' , sep='')
    print('-', format('27',' ^4'), format('28', ' ^3'), format('29', ' ^3'), format('30',' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 3 and days == 29:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('',' ^4'), format('', ' ^3'), format('01', ' ^3'), format('02',' ^3'), format('03',' ^3'), format('04',' ^3'), format('05',' ^3'), '-' , sep='')
    print('-', format('06',' ^4'), format('07', ' ^3'), format('08', ' ^3'), format('09',' ^3'), format('10',' ^3'), format('11',' ^3'), format('12',' ^3'), '-' , sep='')
    print('-', format('13',' ^4'), format('14', ' ^3'), format('15', ' ^3'), format('16',' ^3'), format('17',' ^3'), format('18',' ^3'), format('19',' ^3'), '-' , sep='')
    print('-', format('20',' ^4'), format('21', ' ^3'), format('22', ' ^3'), format('23',' ^3'), format('24',' ^3'), format('25',' ^3'), format('26',' ^3'), '-' , sep='')
    print('-', format('27',' ^4'), format('28', ' ^3'), format('29', ' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 3 and days == 28:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('',' ^4'), format('', ' ^3'), format('01', ' ^3'), format('02',' ^3'), format('03',' ^3'), format('04',' ^3'), format('05',' ^3'), '-' , sep='')
    print('-', format('06',' ^4'), format('07', ' ^3'), format('08', ' ^3'), format('09',' ^3'), format('10',' ^3'), format('11',' ^3'), format('12',' ^3'), '-' , sep='')
    print('-', format('13',' ^4'), format('14', ' ^3'), format('15', ' ^3'), format('16',' ^3'), format('17',' ^3'), format('18',' ^3'), format('19',' ^3'), '-' , sep='')
    print('-', format('20',' ^4'), format('21', ' ^3'), format('22', ' ^3'), format('23',' ^3'), format('24',' ^3'), format('25',' ^3'), format('26',' ^3'), '-' , sep='')
    print('-', format('27',' ^4'), format('28', ' ^3'), format('', ' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 4 and days == 31:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('',' ^4'), format('', ' ^3'), format('', ' ^3'), format('01',' ^3'), format('02',' ^3'), format('03',' ^3'), format('04',' ^3'), '-' , sep='')
    print('-', format('05',' ^4'), format('06', ' ^3'), format('07', ' ^3'), format('08',' ^3'), format('09',' ^3'), format('10',' ^3'), format('11',' ^3'), '-' , sep='')
    print('-', format('12',' ^4'), format('13', ' ^3'), format('14', ' ^3'), format('15',' ^3'), format('16',' ^3'), format('17',' ^3'), format('18',' ^3'), '-' , sep='')
    print('-', format('19',' ^4'), format('20', ' ^3'), format('21', ' ^3'), format('22',' ^3'), format('23',' ^3'), format('24',' ^3'), format('25',' ^3'), '-' , sep='')
    print('-', format('26',' ^4'), format('27', ' ^3'), format('28', ' ^3'), format('29',' ^3'), format('30',' ^3'), format('31',' ^3'), format('',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 4 and days == 30:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('',' ^4'), format('', ' ^3'), format('', ' ^3'), format('01',' ^3'), format('02',' ^3'), format('03',' ^3'), format('04',' ^3'), '-' , sep='')
    print('-', format('05',' ^4'), format('06', ' ^3'), format('07', ' ^3'), format('08',' ^3'), format('09',' ^3'), format('10',' ^3'), format('11',' ^3'), '-' , sep='')
    print('-', format('12',' ^4'), format('13', ' ^3'), format('14', ' ^3'), format('15',' ^3'), format('16',' ^3'), format('17',' ^3'), format('18',' ^3'), '-' , sep='')
    print('-', format('19',' ^4'), format('20', ' ^3'), format('21', ' ^3'), format('22',' ^3'), format('23',' ^3'), format('24',' ^3'), format('25',' ^3'), '-' , sep='')
    print('-', format('26',' ^4'), format('27', ' ^3'), format('28', ' ^3'), format('29',' ^3'), format('30',' ^3'), format('',' ^3'), format('',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 4 and days == 29:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('',' ^4'), format('', ' ^3'), format('', ' ^3'), format('01',' ^3'), format('02',' ^3'), format('03',' ^3'), format('04',' ^3'), '-' , sep='')
    print('-', format('05',' ^4'), format('06', ' ^3'), format('07', ' ^3'), format('08',' ^3'), format('09',' ^3'), format('10',' ^3'), format('11',' ^3'), '-' , sep='')
    print('-', format('12',' ^4'), format('13', ' ^3'), format('14', ' ^3'), format('15',' ^3'), format('16',' ^3'), format('17',' ^3'), format('18',' ^3'), '-' , sep='')
    print('-', format('19',' ^4'), format('20', ' ^3'), format('21', ' ^3'), format('22',' ^3'), format('23',' ^3'), format('24',' ^3'), format('25',' ^3'), '-' , sep='')
    print('-', format('26',' ^4'), format('27', ' ^3'), format('28', ' ^3'), format('29',' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 4 and days == 28:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('',' ^4'), format('', ' ^3'), format('', ' ^3'), format('01',' ^3'), format('02',' ^3'), format('03',' ^3'), format('04',' ^3'), '-' , sep='')
    print('-', format('05',' ^4'), format('06', ' ^3'), format('07', ' ^3'), format('08',' ^3'), format('09',' ^3'), format('10',' ^3'), format('11',' ^3'), '-' , sep='')
    print('-', format('12',' ^4'), format('13', ' ^3'), format('14', ' ^3'), format('15',' ^3'), format('16',' ^3'), format('17',' ^3'), format('18',' ^3'), '-' , sep='')
    print('-', format('19',' ^4'), format('20', ' ^3'), format('21', ' ^3'), format('22',' ^3'), format('23',' ^3'), format('24',' ^3'), format('25',' ^3'), '-' , sep='')
    print('-', format('26',' ^4'), format('27', ' ^3'), format('28', ' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 5 and days == 31:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('',' ^4'), format('', ' ^3'), format('', ' ^3'), format('',' ^3'), format('01',' ^3'), format('02',' ^3'), format('03',' ^3'), '-' , sep='')
    print('-', format('04',' ^4'), format('05', ' ^3'), format('06', ' ^3'), format('07',' ^3'), format('08',' ^3'), format('09',' ^3'), format('10',' ^3'), '-' , sep='')
    print('-', format('11',' ^4'), format('12', ' ^3'), format('13', ' ^3'), format('14',' ^3'), format('15',' ^3'), format('16',' ^3'), format('17',' ^3'), '-' , sep='')
    print('-', format('18',' ^4'), format('19', ' ^3'), format('20', ' ^3'), format('21',' ^3'), format('22',' ^3'), format('23',' ^3'), format('24',' ^3'), '-' , sep='')
    print('-', format('25',' ^4'), format('26', ' ^3'), format('27', ' ^3'), format('28',' ^3'), format('29',' ^3'), format('30',' ^3'), format('31',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 5 and days == 30:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('',' ^4'), format('', ' ^3'), format('', ' ^3'), format('',' ^3'), format('01',' ^3'), format('02',' ^3'), format('03',' ^3'), '-' , sep='')
    print('-', format('04',' ^4'), format('05', ' ^3'), format('06', ' ^3'), format('07',' ^3'), format('08',' ^3'), format('09',' ^3'), format('10',' ^3'), '-' , sep='')
    print('-', format('11',' ^4'), format('12', ' ^3'), format('13', ' ^3'), format('14',' ^3'), format('15',' ^3'), format('16',' ^3'), format('17',' ^3'), '-' , sep='')
    print('-', format('18',' ^4'), format('19', ' ^3'), format('20', ' ^3'), format('21',' ^3'), format('22',' ^3'), format('23',' ^3'), format('24',' ^3'), '-' , sep='')
    print('-', format('25',' ^4'), format('26', ' ^3'), format('27', ' ^3'), format('28',' ^3'), format('29',' ^3'), format('30',' ^3'), format('',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 5 and days == 29:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('',' ^4'), format('', ' ^3'), format('', ' ^3'), format('',' ^3'), format('01',' ^3'), format('02',' ^3'), format('03',' ^3'), '-' , sep='')
    print('-', format('04',' ^4'), format('05', ' ^3'), format('06', ' ^3'), format('07',' ^3'), format('08',' ^3'), format('09',' ^3'), format('10',' ^3'), '-' , sep='')
    print('-', format('11',' ^4'), format('12', ' ^3'), format('13', ' ^3'), format('14',' ^3'), format('15',' ^3'), format('16',' ^3'), format('17',' ^3'), '-' , sep='')
    print('-', format('18',' ^4'), format('19', ' ^3'), format('20', ' ^3'), format('21',' ^3'), format('22',' ^3'), format('23',' ^3'), format('24',' ^3'), '-' , sep='')
    print('-', format('25',' ^4'), format('26', ' ^3'), format('27', ' ^3'), format('28',' ^3'), format('29',' ^3'), format('',' ^3'), format('',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 5 and days == 28:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('',' ^4'), format('', ' ^3'), format('', ' ^3'), format('',' ^3'), format('01',' ^3'), format('02',' ^3'), format('03',' ^3'), '-' , sep='')
    print('-', format('04',' ^4'), format('05', ' ^3'), format('06', ' ^3'), format('07',' ^3'), format('08',' ^3'), format('09',' ^3'), format('10',' ^3'), '-' , sep='')
    print('-', format('11',' ^4'), format('12', ' ^3'), format('13', ' ^3'), format('14',' ^3'), format('15',' ^3'), format('16',' ^3'), format('17',' ^3'), '-' , sep='')
    print('-', format('18',' ^4'), format('19', ' ^3'), format('20', ' ^3'), format('21',' ^3'), format('22',' ^3'), format('23',' ^3'), format('24',' ^3'), '-' , sep='')
    print('-', format('25',' ^4'), format('26', ' ^3'), format('27', ' ^3'), format('28',' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 6 and days == 31:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('',' ^4'), format('', ' ^3'), format('', ' ^3'), format('',' ^3'), format('',' ^3'), format('01',' ^3'), format('02',' ^3'), '-' , sep='')
    print('-', format('03',' ^4'), format('04', ' ^3'), format('05', ' ^3'), format('06',' ^3'), format('07',' ^3'), format('08',' ^3'), format('09',' ^3'), '-' , sep='')
    print('-', format('10',' ^4'), format('11', ' ^3'), format('12', ' ^3'), format('13',' ^3'), format('14',' ^3'), format('15',' ^3'), format('16',' ^3'), '-' , sep='')
    print('-', format('17',' ^4'), format('18', ' ^3'), format('19', ' ^3'), format('20',' ^3'), format('21',' ^3'), format('22',' ^3'), format('23',' ^3'), '-' , sep='')
    print('-', format('24',' ^4'), format('25', ' ^3'), format('26', ' ^3'), format('27',' ^3'), format('28',' ^3'), format('29',' ^3'), format('30',' ^3'), '-' , sep='')
    print('-', format('31',' ^4'), format('', ' ^3'), format('', ' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 6 and days == 30:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('',' ^4'), format('', ' ^3'), format('', ' ^3'), format('',' ^3'), format('',' ^3'), format('01',' ^3'), format('02',' ^3'), '-' , sep='')
    print('-', format('03',' ^4'), format('04', ' ^3'), format('05', ' ^3'), format('06',' ^3'), format('07',' ^3'), format('08',' ^3'), format('09',' ^3'), '-' , sep='')
    print('-', format('10',' ^4'), format('11', ' ^3'), format('12', ' ^3'), format('13',' ^3'), format('14',' ^3'), format('15',' ^3'), format('16',' ^3'), '-' , sep='')
    print('-', format('17',' ^4'), format('18', ' ^3'), format('19', ' ^3'), format('20',' ^3'), format('21',' ^3'), format('22',' ^3'), format('23',' ^3'), '-' , sep='')
    print('-', format('24',' ^4'), format('25', ' ^3'), format('26', ' ^3'), format('27',' ^3'), format('28',' ^3'), format('29',' ^3'), format('30',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 6 and days == 29:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('',' ^4'), format('', ' ^3'), format('', ' ^3'), format('',' ^3'), format('',' ^3'), format('01',' ^3'), format('02',' ^3'), '-' , sep='')
    print('-', format('03',' ^4'), format('04', ' ^3'), format('05', ' ^3'), format('06',' ^3'), format('07',' ^3'), format('08',' ^3'), format('09',' ^3'), '-' , sep='')
    print('-', format('10',' ^4'), format('11', ' ^3'), format('12', ' ^3'), format('13',' ^3'), format('14',' ^3'), format('15',' ^3'), format('16',' ^3'), '-' , sep='')
    print('-', format('17',' ^4'), format('18', ' ^3'), format('19', ' ^3'), format('20',' ^3'), format('21',' ^3'), format('22',' ^3'), format('23',' ^3'), '-' , sep='')
    print('-', format('24',' ^4'), format('25', ' ^3'), format('26', ' ^3'), format('27',' ^3'), format('28',' ^3'), format('29',' ^3'), format('',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 6 and days == 28:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('',' ^4'), format('', ' ^3'), format('', ' ^3'), format('',' ^3'), format('',' ^3'), format('01',' ^3'), format('02',' ^3'), '-' , sep='')
    print('-', format('03',' ^4'), format('04', ' ^3'), format('05', ' ^3'), format('06',' ^3'), format('07',' ^3'), format('08',' ^3'), format('09',' ^3'), '-' , sep='')
    print('-', format('10',' ^4'), format('11', ' ^3'), format('12', ' ^3'), format('13',' ^3'), format('14',' ^3'), format('15',' ^3'), format('16',' ^3'), '-' , sep='')
    print('-', format('17',' ^4'), format('18', ' ^3'), format('19', ' ^3'), format('20',' ^3'), format('21',' ^3'), format('22',' ^3'), format('23',' ^3'), '-' , sep='')
    print('-', format('24',' ^4'), format('25', ' ^3'), format('26', ' ^3'), format('27',' ^3'), format('28',' ^3'), format('',' ^3'), format('',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 0 and days == 31:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('',' ^4'), format('', ' ^3'), format('', ' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), format('01',' ^3'), '-' , sep='')
    print('-', format('02',' ^4'), format('03', ' ^3'), format('04', ' ^3'), format('05',' ^3'), format('06',' ^3'), format('07',' ^3'), format('08',' ^3'), '-' , sep='')
    print('-', format('09',' ^4'), format('10', ' ^3'), format('11', ' ^3'), format('12',' ^3'), format('13',' ^3'), format('14',' ^3'), format('15',' ^3'), '-' , sep='')
    print('-', format('16',' ^4'), format('17', ' ^3'), format('18', ' ^3'), format('19',' ^3'), format('20',' ^3'), format('21',' ^3'), format('22',' ^3'), '-' , sep='')
    print('-', format('23',' ^4'), format('24', ' ^3'), format('25', ' ^3'), format('26',' ^3'), format('27',' ^3'), format('28',' ^3'), format('29',' ^3'), '-' , sep='')
    print('-', format('30',' ^4'), format('31', ' ^3'), format('', ' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 0 and days == 30:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('',' ^4'), format('', ' ^3'), format('', ' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), format('01',' ^3'), '-' , sep='')
    print('-', format('02',' ^4'), format('03', ' ^3'), format('04', ' ^3'), format('05',' ^3'), format('06',' ^3'), format('07',' ^3'), format('08',' ^3'), '-' , sep='')
    print('-', format('09',' ^4'), format('10', ' ^3'), format('11', ' ^3'), format('12',' ^3'), format('13',' ^3'), format('14',' ^3'), format('15',' ^3'), '-' , sep='')
    print('-', format('16',' ^4'), format('17', ' ^3'), format('18', ' ^3'), format('19',' ^3'), format('20',' ^3'), format('21',' ^3'), format('22',' ^3'), '-' , sep='')
    print('-', format('23',' ^4'), format('24', ' ^3'), format('25', ' ^3'), format('26',' ^3'), format('27',' ^3'), format('28',' ^3'), format('29',' ^3'), '-' , sep='')
    print('-', format('30',' ^4'), format('', ' ^3'), format('', ' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 0 and days == 29:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('',' ^4'), format('', ' ^3'), format('', ' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), format('01',' ^3'), '-' , sep='')
    print('-', format('02',' ^4'), format('03', ' ^3'), format('04', ' ^3'), format('05',' ^3'), format('06',' ^3'), format('07',' ^3'), format('08',' ^3'), '-' , sep='')
    print('-', format('09',' ^4'), format('10', ' ^3'), format('11', ' ^3'), format('12',' ^3'), format('13',' ^3'), format('14',' ^3'), format('15',' ^3'), '-' , sep='')
    print('-', format('16',' ^4'), format('17', ' ^3'), format('18', ' ^3'), format('19',' ^3'), format('20',' ^3'), format('21',' ^3'), format('22',' ^3'), '-' , sep='')
    print('-', format('23',' ^4'), format('24', ' ^3'), format('25', ' ^3'), format('26',' ^3'), format('27',' ^3'), format('28',' ^3'), format('29',' ^3'), '-' , sep='')
    print(format('-','-^24'))
elif value == 0 and days == 28:
    print(format('-','-^24'))
    print('-' , format(month," ^16"), format(year,' >6'), '-' , sep='') 
    print(format('-','-^24'))
    print('-', format('Sn',' ^4'), format('M', ' ^3'), format('T', ' ^3'), format('W',' ^3'), format('Th',' ^3'), format('F',' ^3'), format('Sa',' ^3'), '-' , sep='')
    print('-', format('',' ^4'), format('', ' ^3'), format('', ' ^3'), format('',' ^3'), format('',' ^3'), format('',' ^3'), format('01',' ^3'), '-' , sep='')
    print('-', format('02',' ^4'), format('03', ' ^3'), format('04', ' ^3'), format('05',' ^3'), format('06',' ^3'), format('07',' ^3'), format('08',' ^3'), '-' , sep='')
    print('-', format('09',' ^4'), format('10', ' ^3'), format('11', ' ^3'), format('12',' ^3'), format('13',' ^3'), format('14',' ^3'), format('15',' ^3'), '-' , sep='')
    print('-', format('16',' ^4'), format('17', ' ^3'), format('18', ' ^3'), format('19',' ^3'), format('20',' ^3'), format('21',' ^3'), format('22',' ^3'), '-' , sep='')
    print('-', format('23',' ^4'), format('24', ' ^3'), format('25', ' ^3'), format('26',' ^3'), format('27',' ^3'), format('28',' ^3'), format('',' ^3'), '-' , sep='')
    print(format('-','-^24'))
