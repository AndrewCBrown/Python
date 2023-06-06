#"E" removal program by Andrew Brown 11/15/2018

#Open files
file="Text.txt"
newfile="Text without e.txt"

input_file=open(file,"r")
output_file=open(newfile,"w")

#Iterate through the string in the file
total_qty=0
total_length=0
for line in input_file:
    length=len(line)
    total_length+=length
    #Count the "E"'s and "e"'s
    E_qty=line.count("E")
    e_qty=line.count("e")
    qty=E_qty+e_qty
    total_qty+=qty
    #Remove the "E"'s and "e"'s after they have been counted
    new_line=line.replace("E","")
    new_line=new_line.replace("e","")
    #Write the new line without "E" or "e"
    output_file.write(new_line)

#Calculate percentage
percentage=(total_qty/total_length)*100

#Print the occurances of "E" and "e" originally, and what % of the text that was.
print("The characters 'E' and 'e' together occured",total_qty,"times!")
print("Which was ",percentage,"% of the total text file.",sep="")
output_file.close()
output_file=open(newfile,"r")
for line in output_file:
    print(line)

#Close files
input_file.close()
output_file.close()
