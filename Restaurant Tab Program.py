#Restaurant Tab program by Andrew Brown 9/6/2018

#Greeting
print("Welcome to the restaurant tab calculator!\nThis is a fast and easy way to know your total bill and a recommended tip.")
print("All you have to do is enter the price of your items and it will do the rest!")
print("\n")

#Ask for entree price
entree=float(input("What is the total price of your entrees?:"))

#Ask for appetizer price
appetizer=float(input("What is the total price of your appetizers?:"))

#Ask for drink price
drink=float(input("What is the total price of your drinks?:"))

#Ask for dessert price
dessert=float(input("What is the total price of your desserts?:"))

#Calculations
subTotal=entree+appetizer+drink+dessert
tax=0.094*float(subTotal)
total=float(tax)+float(subTotal)
tip15=float(total)*0.15
tip18=float(total)*0.18
tip20=float(total)*0.2

#Print Final Tab
print("\n")
print(format("Entrees",".<25"),"$",format(entree,".2f"),sep="")
print(format("Appetizers",".<25"),"$",format(appetizer,".2f"),sep="")
print(format("Drinks",".<25"),"$",format(drink,".2f"),sep="")
print(format("Desserts",".<25"),"$",format(dessert,".2f"),sep="")
print(format("-","-^31"))
print(format("SubTotal",".<25"),"$",format(subTotal,".2f"),sep="")
print(format("Tax",".<25"),"$",format(tax,".2f"),sep="")
print(format("-","-^31"))
print(format("Total",".<25"),"$",format(total,".2f"),sep="")
print("")
print(format("Tip(15%)",".<25"),"$",format(tip15,".2f"),sep="")
print(format("Tip(18%)",".<25"),"$",format(tip18,".2f"),sep="")
print(format("Tip(20%)",".<25"),"$",format(tip20,".2f"),sep="")



    
