#Grocery List Program by Andrew Brown 10/2/2018

#Greeting
print("Welcome to the grocery list program!")
print("In this program you will enter everything on your grocery list\nand then type 'done' when finished.")

#Identifying variables
groceryList=[]

#User Input
item=input("What is an item you need to buy?: ")

while (item!="done"):
    groceryList.append(item)
    item=input("What is another item you need to buy?: ")

#Offer to sort list
sortList=input("Would you like to sort your grocery list alphabetically? ('Yes' or 'No): ")
while (sortList not in("Yes","No","yes","no")):
    print("Invalid entry, try again!")
    sortList=input()
if (sortList=="Yes" or sortList=="yes"):
    groceryList.sort()

#Print List
print("\nHere is your list!\n",groceryList)

#Go Through List
obtained=0
print("\nNow you will be given the items on your grocery list one at a\ntime and you can type 'y' when you have the item!\nIf you want to get the item later type 'skip'.\n")

while (len(groceryList)>groceryList.count("bought")):
    for item in groceryList:
        if item!="bought":
            print("Go get: ",item,"! ",sep="")
            obtained=input()
            while (obtained!='y' and obtained!='skip'):
                print("Invalid entry, try again!")
                obtained=input()
            if (obtained=="y"):
                x=groceryList.index(item)
                del groceryList[x]
                groceryList.insert(x,"bought")

#Completion
print("You got everything on your list!")
                  

#I think these two lines would do the same thing
#groceryList.remove(item)
#del groceryList[groceryList.index(item)]
