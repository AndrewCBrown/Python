#Chess Program by Andrew Brown 9/15/2018

#Greeting
print("This program is designed to calculate how many pounds of wheat there\nwould be if someone were to put 1 grain on the first square in a\nchess board, and then put double that ammount for every next square.\n")

#Calculations
grainsT=int((2**64)-1)
weight=grainsT/7000

#Print Result
print("There would be",format(weight,".0f"),"pounds of wheat!")
