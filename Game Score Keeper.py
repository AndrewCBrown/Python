#Score keeping program for family games
#Andrew Brown
#Started 12/22/2018

###Try to put everything in a loop so there can be master commands that can
###edit previous entries or change player names or delete or add players
###without having to restart the program

###Maybe have like a way to escape but then return to the same spot so
###when you've escaped you have all the master controls and can view everything

#Define methods of score adding that would be common so they can be called in the different game functions
#Define the different games the program works for as functions

def MT_message(i):
    if i==0:
        message="This round you are looking for the double twelve!"
    elif i==1:
        message="This round you are looking for the double eleven!"
    elif i==2:
        message="This round you are looking for the double ten!"
    elif i==3:
        message="This round you are looking for the double nine!"
    elif i==4:
        message="This round you are looking for the double eight!"
    elif i==5:
        message="This round you are looking for the double seven!"
    elif i==6:
        message="This round you are looking for the double six!",chr(9861),chr(9861)
    elif i==7:
        message="This round you are looking for the double five!",chr(9860),chr(9860)
    elif i==8:
        message="This round you are looking for the double four!",chr(9859),chr(9859)
    elif i==9:
        message="This round you are looking for the double three!",chr(9858),chr(9858)
    elif i==10:
        message="This round you are looking for the double two!",chr(9857),chr(9857)
    elif i==11:
        message="This round you are looking for the double one!",chr(9856),chr(9856)
    elif i==12:
        message="This is the final round! You are looking for the double blank!"
    return message

def MT_player_header(player_list,player_number):
    line=""
    for i in range(player_number):
        line+=(format(player_list[i],"^11"))
    print(line)

def MT_scoreboard_display(player_list,player_number,i,x,scoreboard):
    for rounds in range(i+1):
        line=""
        for players in range(player_number):
            line+=(format(scoreboard[rounds][players],"^11"))
        print(line)

def MT_ranking(player_list,player_number,i,x,scoreboard):
    total_scores=[]
    for player in range(player_number):
        Sum=0
        for loop in range(i+1):
            Sum+=scoreboard[loop][player]
        total_scores.append(Sum)
    for foo in range(player_number):
        minimum=min(total_scores)
        spot=total_scores.index(minimum)
        print(total_scores[spot],player_list[spot])
        total_scores[spot]=999999

def MT_master_controls(scoreboard,x):
    command=input("Give a command")
    while command=="edit_score":
        score=int(input())
        row=int(input())
        column=int(input())
        scoreboard[row][column]=score
        command=input("Give a command")
    print("What did ",player_list[x]," score in this round?",sep="")
    score=input()
    return score, scoreboard

def Mexican_Train(player_list,player_number):
    scoreboard=[]
    scoreRow=[]
    for foo in range(player_number):
        scoreRow.append(0)        
    for i in range(13):
        scoreboard.append(scoreRow[0:player_number])
        print("~~~Round ",(i+1),"~~~",sep="")
        print(MT_message(i))
        for x in range(player_number):
            print("What did ",player_list[x]," score in this round?",sep="")
            score=input()
            if score=="hack":
                score, scoreboard=MT_master_controls(scoreboard,x)
            if score=="":
                score=0
            score=int(score)
            scoreboard[i][x]=score
        MT_player_header(player_list,player_number)
        MT_scoreboard_display(player_list,player_number,i,x,scoreboard)
        print("These are the current standings!")
        MT_ranking(player_list,player_number,i,x,scoreboard)

#Ask user what game they are playing
print("List of current games available for automatic scoring:")
print("Mexican Train")
print("Please type in the name of the game exactly as listed above.")
game=input("What game are you playing?: ")

#Ask user for players names in successive order, starting with first dealer
#user will enter done when all players have been added
print("Now you will enter all player's names starting with\nthe first player (the first dealer) and moving through\nall players in a clockwise fashion.")
player="_"
player_list=[]
while player!="":
    player=str(input("Enter a player's name(Press enter twice when the last player has been typed): "))
    while len(player)>10:
        print("Player names must be 10 characters or less! Try again!\n")
        player=str(input("Enter a player's name(Press enter twice when the last player has been typed): "))
    player_list.append(player)
del player_list[(len(player_list)-1)]
player_number=len(player_list)
print(player_list)

#Loop through, continually asking for players scores and giving updates and stats
if game=="Mexican Train":
    Mexican_Train(player_list,player_number)
