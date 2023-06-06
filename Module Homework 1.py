#Write a function called convertStatus that is passed status code ' f', ' s', ' j', or ' r' and returns the
#string ' freshman', ' sophomore', ' junior', or ' senior', respectively.
#Design your function so that if an inappropriate letter is passed, an error value is returned.
#Make sure to include an appropriate docstring with your function.

def convertStatus(letter):
    """This function converts the string 'f' to 'freshman',
    's' to 'sophomore', 'j' to 'junior,
    and 'r' to 'senior'. If anything else is passed
    then an error message is returned."""
    while letter not in ("f","s","j","r"):
        print("That is not a valid entry! Try again.\nEnter 'f', 's', 'j', or 'r' for freshman, sophomore, junior, and senior respectively.")
        letter=str(input(""))
    if letter=="f":
        return "freshman"
    elif letter=="s":
        return "sophomore"
    elif letter=="j":
        return "junior"
    elif letter=="r":
        return "senior"


letter=str(input("Enter 'f', 's', 'j', or 'r' for freshman, sophomore, junior, and senior respectively."))
year=convertStatus(letter)
print(year)
