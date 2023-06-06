#Edit the palindromeChecker code by adding an additional function which removes the
#spaces and punctuation from a sentence to check it as a palindrome.
#The original code can be found here on Moodle.

def clean(word):
    if word.isalpha():
        return word
    word=word.replace(" ","")
    word=word.replace("!","")
    word=word.replace(",","")
    word=word.replace(".","")
    word=word.replace("`","")
    word=word.replace("~","")
    word=word.replace("#","")
    word=word.replace("'","")
    word=word.replace(":","")
    word=word.replace(";","")
    return word

def oddCheck(word):
    """return number of characters
    return True if odd"""
    num_chars=len(word)
    if len(word)%2==1:
        odd=True
    else:
        odd=False
    return [num_chars, odd]

def createStack(word):
    """Returns the last half of the string pushed to the satck."""
    lasthalf=[]
    Word=word
    if len(Word)%2==1:
        i=int((len(Word)/2)+.5)-1
        for z in range(i):
            item=Word[(len(Word)-1)]
            lasthalf.append(item)
            a=len(Word)
            List=[]
            for b in range(a):
                List.append(Word[b])
            del List[(len(Word)-1)]
            c=0
            Word=""
            a=len(List)
            for c in range(a):
                Word=Word+List[c]
    else:
        i=int((len(Word)/2))-1
        for z in range(i):
            item=Word[(len(Word)-1)]
            lasthalf.append(item)
            a=len(Word)
            List=[]
            for b in range(a):
                List.append(Word[b])
            del List[(len(Word)-1)]
            c=0
            Word=""
            a=len(List)
            for c in range(a):
                Word=Word+List[c]
    return lasthalf

def checkStack(word,lasthalf):
    """Returns True if word is a palindrome."""
    x=0
    counter=0
    i=len(lasthalf)
    while x!=i and word[x]==lasthalf[x]:
        counter=counter+1
        x=x+1
    if counter==i:
        palindrome=True
    else:
        palindrome=False
    return palindrome


#~~~~~~~~~~~MAIN~~~~~~~~~~~
print("This program will check to see if a given string is a palindrome")
print("Enter the empty string to exit.")

empty_string=''
word=str(input("What string would you like to check?"))

while word != empty_string:
    word=clean(word)
    [num_chars, odd] = oddCheck(word)
    if num_chars == 1:
        print("Of course it's a palindrome, are you kidding?")
    else:
        lasthalf=createStack(word)
        palindrome=checkStack(word,lasthalf)
        if palindrome:
            print(word+" is a palindrome!")
        else:
            print(word+" is not a palindrome!")
    word=str(input("What string would you like to check next?"))
print("Thanks for using palindrome.")
