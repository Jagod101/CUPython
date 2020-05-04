#Zach Jagoda and Daniel Kavesh
#Student ID: 2274813 and 2314750
#Student Email: jagod101@mail.chapman.edu and kavesh@chapman.edu
#CPSC230
#Assignment 5

#Ask the user to make one of two choices...destruct or construct
#If the user chooses destruct, prompt them for an alternade, and then output the 2 words from that alternade
#If the user chooses construct, prompt them for 2 words, and then output the alternade thatwould have produced those words

#Import Libraries from Itertools for Combination https://docs.python.org/2/library/itertools.html
from itertools import chain
from itertools import zip_longest

#Declare variables
userInput = 0
alternade = ""
wordOne = ""
wordTwo = ""
hasNumbers = False

#Function to Destruct an Alternade
def destruct(alternade):
    wordOne = alternade[::2]    #Word One set to take every other character starting from 0
    wordTwo = alternade[1::2]   #Word Two set to take every other character starting from 1
    print("Your Alternade Formed Two Words: ", wordOne,"and", wordTwo)
    return

#Function to Construct an Alternade
def construct(wordOne, wordTwo):
    newAlternade = ""

    newAlternade = "".join(chain.from_iterable(zip_longest(wordOne, wordTwo, fillvalue = "")))  #Alternates between both words, and fills in the empty value if the words are not the same length
    print("Your Two Words Formed an Alternade: ", newAlternade)

    return

#Program Loop
while True:
    #User Input for what they want the program to do
    userInput = int(input("Please choose between [1] Destruct, [2] Construct, or [3] Exit Program: "))

    #Option 1 - Destruct
    if userInput == 1:
        alternade = input("Please Enter an Alternade: ")

        #If a Word is enetered with characteers that are not a letter, break
        hasNumbers = any(char.isdigit() for char in alternade)
        if hasNumbers == True:
            print("Please Try Again with an Alternade that has no Numbers")
            break

        destruct(alternade)
        userInput = 0

    #Option 2- Construct
    elif userInput == 2:
        wordOne = input("Please Enter Your First Word: ")

        #If a Word is enetered with characteers that are not a letter, break
        hasNumbers = any(char.isdigit() for char in wordOne)
        if hasNumbers == True:
            print("Please Try Again with a Word that has no Numbers")
            break

        wordTwo = input("Please Enter Your Second Word: ")

        #If a Word is enetered with characteers that are not a letter, break
        hasNumbers = any(char.isdigit() for char in wordTwo)
        if hasNumbers == True:
            print("Please Try Again with a Word that has no Numbers")
            break

        construct(wordOne, wordTwo)
        userInput = 0

    #Option 3 - Exit
    elif userInput == 3:
        print("Thank you for using our program")
        break

    #Else - Invalid Input (Try Again)
    else:
        print("Please Enter a Valid Option: ")
        continue
