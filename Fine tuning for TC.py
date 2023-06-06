#All this is to fix our issues of the game not ending when you win, and how it uses a guess when you guess somewhere you alreay did instead of just telling you to reguess.

#Define chestsfound equal to 0
chestsfound=0
    
#Define cheststotal to be the number of chests, do this in the same line they are choosing the difficulty.
#so in the if difficulty==easy suite add another line that sets the number of cheststotal
    
#When they find a chest and we're printing "you found one!" also add 1 to variable chestsfound
chestsfound=chestsfound+1

#When they guess somewhere they already guessed, in that suite add the line "i=i-1" to the bottom

#New loop to replace the old
i=0
while i<15 and chestsfound<cheststotal:
    #do the loop here
    #at the end of the loop add 1 to i
    i=i+1

#Delete the "game over" thing all 3 times, then after the loop has closed put this block
if chestsfound==cheststotal and difficulty==hard and i<0:
    print("Congratulations you found all the chests!")
    print("Cheat code: When you are prompted for the row you want, type '#BakerThought' and you will have unlimited guesses!")
    print("Cheat code 2: When you are prompted for the row you want, type 'peep' and it will reveal where all the chests are hiding!")
elif chestsfound==cheststotal and difficulty==hard:
    print("Congratulations you found all the chests!")
    print("Cheat code: When you are prompted for the row you want, type '#BakerThought' and you will have unlimited guesses!")
elif chestsfound==cheststotal:
    print("Congratulations you found all the chests!")
    print("Cheat code: When you are prompted for the row you want, type 'cloumn' and you will receive a special message!")
else:
    print("Game Over!\nBetter luck next time!")





#Now to add the cheats
#In definition of the function row_change is where we add the lines for the cheats
#In the main funciton we'll need to move where we call the row_change function, we need to put it before we ask the user for a column(clomun)

#So for the infinite guesses cheat (this is in the row_change function)
if row=="#BakerThought":
    i=i-99
    print("\n~Infinite guesses turned on~\n")
    row=str(input("Enter which row you would like to pick from "))
    row=row_change(row)
    

#So for the reveal the chests cheat
if row=="peep":
    print("This is where the chests are hiding!")
    if diff=="easy":
        EASY(hidden_easy)
    elif diff=="medium":
        MEDIUM(hidden_medium)
    elif diff=="hard":
        HARD(hidden_hard)
    i=i-1
    row=str(input("Enter which row you would like to pick from "))
    row=row_change(row)

if row=="cloumn":
    print("\n~Hayden is a dingus!~\n")
    i=i-1
    row=str(input("Enter which row you would like to pick from "))
    row=row_change(row)

if row=="420":
    print("\nSmoke weed everyday\n")
    i=i-1
    row=str(input("Enter which row you would like to pick from "))
    row=row_change(row)
