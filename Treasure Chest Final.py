#Greeting
print(format("~","~>35"))
print(format("Welcome to Treasure Hunt!","~^35"))
print(format("~","~>35"))
print("")

import random

#Define function for resetting the easy difficulty
def reset_easy():
    Easy=[["O","O","O"],["O","O","O"],["O","O","O"]]
    
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
    return [Easy,hidden_easy]

#Define function for resetting the medium difficulty
def reset_medium():
    Medium=[["O","O","O","O"],["O","O","O","O"],["O","O","O","O"],["O","O","O","O"]]

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
    return [Medium,hidden_medium]

#Define function for resetting the hard difficulty
def reset_hard():
    Hard=[["O","O","O","O","O"],["O","O","O","O","O"],["O","O","O","O","O"],["O","O","O","O","O"],["O","O","O","O","O"]]

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
    return [Hard,hidden_hard]

#Format for the Teasure hunt game
#3X3
def EASY(List):
    print(format('', ' ^3'), format('1', ' ^1'), format('', ' ^3'), format('2', ' ^1'), format('', ' ^3'), format('3', ' ^1'), sep = '')
    print(format('A ', ' ^1'), format('[', ' ^1'), format(List[0][0], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[0][1], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[0][2], ' ^1'), format(']', ' ^1'), format('', ' ^1'), sep='')
    print(format('B ', ' ^1'), format('[', ' ^1'), format(List[1][0], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[1][1], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[1][2], ' ^1'), format(']', ' ^1'), format('', ' ^1'), sep='')
    print(format('C ', ' ^1'), format('[', ' ^1'), format(List[2][0], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[2][1], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[2][2], ' ^1'), format(']', ' ^1'), format('', ' ^1'), sep='')

#4X4
def MEDIUM(List):
    print(format('', ' ^3'), format('1', ' ^1'), format('', ' ^3'), format('2', ' ^1'), format('', ' ^3'), format('3', ' ^1'), format('', ' ^3'), format('4', ' ^1'), sep = '')
    print(format('A ', ' ^1'), format('[', ' ^1'), format(List[0][0], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[0][1], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[0][2], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[0][3], ' ^1'), format(']', ' ^1'), format('', ' ^1'), sep='')
    print(format('B ', ' ^1'), format('[', ' ^1'), format(List[1][0], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[1][1], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[1][2], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[1][3], ' ^1'), format(']', ' ^1'), format('', ' ^1'), sep='')
    print(format('C ', ' ^1'), format('[', ' ^1'), format(List[2][0], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[2][1], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[2][2], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[2][3], ' ^1'), format(']', ' ^1'), format('', ' ^1'), sep='')
    print(format('D ', ' ^1'), format('[', ' ^1'), format(List[3][0], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[3][1], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[3][2], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[3][3], ' ^1'), format(']', ' ^1'), format('', ' ^1'), sep='')

#5X5
def HARD(List):
    print(format('', ' ^3'), format('1', ' ^1'), format('', ' ^3'), format('2', ' ^1'), format('', ' ^3'), format('3', ' ^1'), format('', ' ^3'), format('4', ' ^1'), format('', ' ^3'), format('5',' ^1'), sep = '')
    print(format('A ', ' ^1'), format('[', ' ^1'), format(List[0][0], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[0][1], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[0][2], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[0][3], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[0][4], ' ^1'), format(']', ' ^1'), format('', ' ^1'), sep='')
    print(format('B ', ' ^1'), format('[', ' ^1'), format(List[1][0], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[1][1], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[1][2], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[1][3], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[1][4], ' ^1'), format(']', ' ^1'), format('', ' ^1'), sep='')
    print(format('C ', ' ^1'), format('[', ' ^1'), format(List[2][0], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[2][1], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[2][2], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[2][3], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[2][4], ' ^1'), format(']', ' ^1'), format('', ' ^1'), sep='')
    print(format('D ', ' ^1'), format('[', ' ^1'), format(List[3][0], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[3][1], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[3][2], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[3][3], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[3][4], ' ^1'), format(']', ' ^1'), format('', ' ^1'), sep='')
    print(format('E ', ' ^1'), format('[', ' ^1'), format(List[4][0], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[4][1], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[4][2], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[4][3], ' ^1'), format(']', ' ^1'), format('', ' ^1'), format('[', ' ^1'), format(List[4][4], ' ^1'), format(']', ' ^1'), format('', ' ^1'), sep='')

#Row Function
def row_change(row,diff,i):
    if row == "A" or row == "a":
        row = 0
    elif row == "B" or row == "b":
        row = 1
    elif row == "C" or row == "c":
        row = 2
    elif row == "D" or row == "d":
        row = 3
    elif row == "E" or row == "e":
        row = 4
    elif row=="#BakerThought":
        i = i-99
        print("\n~Infinite guesses turned on~")
        row=str(input("\nEnter which row you would like to pick from "))
        newRow=row_change(row,diff,i)
        row=newRow[0]
        i=newRow[1]
    elif row=="peep":
        print("\nThis is where the chests are hiding!")
        if diff=="easy":
            EASY(hidden_easy)
        elif diff=="medium":
            MEDIUM(hidden_medium)
        elif diff=="hard":
            HARD(hidden_hard)
        row=str(input("\nEnter which row you would like to pick from "))
        newRow=row_change(row,diff,i)
        row=newRow[0]
    elif row=="cloumn":
        print("\n~Hayden is a dingus!~")
        row=str(input("\nEnter which row you would like to pick from "))
        newRow=row_change(row,diff,i)
        row=newRow[0]
    elif row=="420":
        print("\nSmoke weed everyday")
        row=str(input("\nEnter which row you would like to pick from "))
        newRow=row_change(row,diff,i)
        row=newRow[0]
    else:
        print("That's not a valid entry!\nTry Again")
        row=str(input("\nEnter which row you would like to pick from "))
        newRow=row_change(row,diff,i)
        row=newRow[0]
    return [row,i]

#Treasure function
def Treasure_easy_finder(row,column,i):
    print("")
    global chestsfound
    global Easy
    global hidden_easy
    if Easy[row][column-1] == "X":
        print("You loser, you already guessed that!")
        i = i-1
    elif Easy[row][column-1] == chr(9818):
        print("You already found that chest!")
        i = i-1
    elif hidden_easy[row][column-1] == chr(9818):
        Easy[row][column-1] = chr(9818)
        print("You got one!")
        chestsfound = chestsfound + 1
    elif Easy[row][column-1] == "O":
        Easy[row][column-1] = "X"
        hidden_easy[row][column-1] = "X"
        print("You didn't find one!")
    return [i,chestsfound,Easy,hidden_easy]

def Treasure_medium_finder(row,column,i):
    print("")
    global chestsfound
    global Medium
    global hidden_medium
    if Medium[row][column-1] == "X":
        print("You loser, you already guessed that!")
        i = i-1
    elif Medium[row][column-1] == chr(9818):
        print("You already found that chest!")
        i = i-1
    elif hidden_medium[row][column-1] == chr(9818):
        Medium[row][column-1] = chr(9818)
        print("You got one!")
        chestsfound = chestsfound + 1
    elif Medium[row][column-1] == "O":
        Medium[row][column-1] = "X"
        hidden_medium[row][column-1] = "X"
        print("You didn't find one!")
    return [i,chestsfound,Medium,hidden_medium]

def Treasure_hard_finder(row,column,i):
    print("")
    global chestsfound
    global Hard
    global hidden_hard
    if Hard[row][column-1] == "X":
        print("You loser, you already guessed that!")
        i = i-1
    elif Hard[row][column-1] == chr(9818):
        print("You already found that chest!")
        i = i-1
    elif hidden_hard[row][column-1] == chr(9818):
        Hard[row][column-1] = chr(9818)
        print("You got one!")
        chestsfound = chestsfound + 1
    elif Hard[row][column-1] == "O":
        Hard[row][column-1] = "X"
        hidden_hard[row][column-1] = "X"
        print("You didn't find one!")
    return [i,chestsfound,Hard,hidden_hard]
        
#Main Function   
def main():
    diff = str(input("Enter if you want an 'easy' 'medium' or 'hard'\ndifficulty or enter 'Done' when finished. "))
    print("")
    global chestsfound
    global Easy
    global hidden_easy
    global Medium
    global hidden_medium
    global Hard
    global hidden_hard
    if diff == "easy":
        resets=reset_easy()
        Easy=resets[0]
        hidden_easy=resets[1]
        chestsfound=0
        cheststotal = 3
        i = 0
        while i<6 and chestsfound<cheststotal:
            EASY(Easy)
            row = str(input("\nEnter which row you would like to pick from "))
            newRow = row_change(row,diff,i)
            row=newRow [0]
            i=newRow[1]
            column = input("Enter which column you would like to pick from ")
            while column not in ("1", "2", "3"):
                print("That is not a valid entry!\nTry again")
                column = input("Enter which column you would like to pick from ")
            column=int(column)
            Set_i_chestsfound=Treasure_easy_finder(row,column,i)
            i=Set_i_chestsfound[0]
            chestsfound=Set_i_chestsfound[1]
            Easy=Set_i_chestsfound[2]
            hidden_easy=Set_i_chestsfound[3]
            i = i + 1
        EASY(Easy)
        if chestsfound==cheststotal:
            print("\nCongratulations you found all the chests!")
            print("\nCheat code: When you are prompted for the row you want,\ntype 'cloumn' and you will receive a special message!")
        else:
            print("Game Over!\nBetter luck next time!") 
        main()        
    elif diff == "medium":
        resets=reset_medium()
        Medium=resets[0]
        hidden_medium=resets[1]
        chestsfound=0
        cheststotal = 4
        i = 0
        while i<10 and chestsfound<cheststotal:
            MEDIUM(Medium)
            row = str(input("\nEnter which row you would like to pick from "))
            newRow = row_change(row,diff,i)
            row=newRow [0]
            i=newRow[1]
            column = input("Enter which column you would like to pick from ")
            while column not in ("1", "2", "3", "4"):
                print("That is not a valid entry!\nTry again")
                column = input("Enter which column you would like to pick from ")
            column=int(column)
            Set_i_chestsfound=Treasure_medium_finder(row,column,i)
            i=Set_i_chestsfound[0]
            chestsfound=Set_i_chestsfound[1]
            Medium=Set_i_chestsfound[2]
            hidden_medium=Set_i_chestsfound[3]
            i = i + 1
        MEDIUM(Medium)
        if chestsfound==cheststotal:
            print("\nCongratulations you found all the chests!")
            print("\nCheat code: When you are prompted for the row you want,\ntype 'cloumn' and you will receive a special message!")
        else:
            print("Game Over!\nBetter luck next time!")
        main()
    elif diff == "hard":
        resets=reset_hard()
        Hard=resets[0]
        hidden_hard=resets[1]
        chestsfound=0
        cheststotal = 5
        i = 0
        while i<15 and chestsfound<cheststotal:
            HARD(Hard)
            row = str(input("\nEnter which row you would like to pick from "))
            newRow = row_change(row,diff,i)
            row=newRow [0]
            i=newRow[1]
            column = input("Enter which column you would like to pick from ")
            while column not in ("1", "2", "3", "4", "5"):
                print("That is not a valid entry!\nTry again")
                column = input("Enter which column you would like to pick from ")
            column=int(column)
            Set_i_chestsfound=Treasure_hard_finder(row,column,i)
            i=Set_i_chestsfound[0]
            chestsfound=Set_i_chestsfound[1]
            Hard=Set_i_chestsfound[2]
            hidden_hard=Set_i_chestsfound[3]
            i = i + 1
        HARD(Hard)
        if chestsfound==cheststotal and i<0:
            print("\nCongratulations you found all the chests!")
            print("\nCheat code: When you are prompted for the row you want,\ntype '#BakerThought' and you will have unlimited guesses!")
            print("Cheat code 2: When you are prompted for the row you want,\ntype 'peep' and it will reveal where all the chests are hiding!")
        elif chestsfound==cheststotal:
            print("\nCongratulations you found all the chests!")
            print("Cheat code: When you are prompted for the row you want,\ntype 'cloumn' and you will receive a special message!")
            print("Cheat code: When you are prompted for the row you want,\ntype '#BakerThought' and you will have unlimited guesses!")
        else:
            print("Game Over!\nBetter luck next time!")
        main()
    elif diff == "Done":
        print("Thanks for Playing Treasure Hunt")
    elif diff != "easy" and diff != "medium" and diff != "hard" and diff != "Done":
        print("Try again")
        main()

    

main()
