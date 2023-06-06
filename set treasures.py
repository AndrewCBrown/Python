import random
#Getting 3 random locations on the easymap and defining hidden_easy
location1=random.randint(0,8)

location2=location1
while location2==location1:
    location2=random.randint(0,8)

location3=location1
while location3==location1 or location3==location2:
    location3=random.randint(0,8)

loc1row=location1//3
loc1col=location1%3
loc2row=location2//3
loc2col=location2%3
loc3row=location3//3
loc3col=location3%3

hidden_easy=[["O","O","O"],["O","O","O"],["O","O","O"]]
hidden_easy[loc1row][loc1col]=chr(9818)
hidden_easy[loc2row][loc2col]=chr(9818)
hidden_easy[loc3row][loc3col]=chr(9818)

#Getting 4 random locations on the mediummap and defining hidden_medium
location1=random.randint(0,15)

location2=location1
while location2==location1:
    location2=random.randint(0,15)

location3=location1
while location3==location1 or location3==location2:
    location3=random.randint(0,15)

location4=location1
while location4==location1 or location4==location2 or location4==location3:
    location4=random.randint(0,15)

loc1row=location1//4
loc1col=location1%4
loc2row=location2//4
loc2col=location2%4
loc3row=location3//4
loc3col=location3%4
loc4row=location4//4
loc4col=location4%4

hidden_medium=[["O","O","O","O"],["O","O","O","O"],["O","O","O","O"],["O","O","O","O"]]
hidden_medium[loc1row][loc1col]=chr(9818)
hidden_medium[loc2row][loc2col]=chr(9818)
hidden_medium[loc3row][loc3col]=chr(9818)
hidden_medium[loc4row][loc4col]=chr(9818)

#Getting 5 random locations on the mediummap and defining hidden_hard
location1=random.randint(0,24)

location2=location1
while location2==location1:
    location2=random.randint(0,24)

location3=location1
while location3==location1 or location3==location2:
    location3=random.randint(0,24)

location4=location1
while location4==location1 or location4==location2 or location4==location3:
    location4=random.randint(0,24)

location5=location1
while location5==location1 or location5==location2 or location5==location3 or location5==location4:
    location5=random.randint(0,24)

loc1row=location1//5
loc1col=location1%5
loc2row=location2//5
loc2col=location2%5
loc3row=location3//5
loc3col=location3%5
loc4row=location4//5
loc4col=location4%5
loc5row=location5//5
loc5col=location5%5

hidden_hard=[["O","O","O","O","O"],["O","O","O","O","O"],["O","O","O","O","O"],["O","O","O","O","O"],["O","O","O","O","O"]]
hidden_hard[loc1row][loc1col]=chr(9818)
hidden_hard[loc2row][loc2col]=chr(9818)
hidden_hard[loc3row][loc3col]=chr(9818)
hidden_hard[loc4row][loc4col]=chr(9818)
hidden_hard[loc5row][loc5col]=chr(9818)





print(hidden_easy)
print(hidden_medium)
print(hidden_hard)

