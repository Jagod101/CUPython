#Zach Jagoda and Daniel Kavesh
#Student ID: 2274813 and 2314750
#Student Email: jagod101@mail.chapman.edu and kavesh@chapman.edu
#CPSC230
#Assignment 5

#Ask the user to make one of two choices...destruct or construct
#If the user chooses destruct, prompt them for an alternade, and then output the 2 words from that alternade
#If the user chooses construct, prompt them for 2 words, and then output the alternade thatwould have produced those words

userInput = 0
alternade = ""
wordOne = ""
wordTwo = ""
hasNumbers = False

lengthOne = 0
lengthTwo = 0
wordLength = 0

def destruct(alternade):
    wordOne = alternade[::2]
    wordTwo = alternade[1::2]
    print("Your Alternade Formed Two Words: ", wordOne,"and", wordTwo)
    return

def construct(wordOne, wordTwo, wordLength):
    count = 0
    newAlternade = ""
    countOne = 0
    countTwo = 0
    for i in range(wordLengthmi):
        if count == 0:
            newAlternade += wordOne[countOne:]
            count = 1
            countOne = countOne + 1
        elif count == 1:
            newAlternade += wordTwo[countTwo:]
            count = 0
            countTwo = countTwo + 1
        else:
            break
    print("Your Two Words Formed an Alternade: ", newAlternade)
    return

while True:
    userInput = int(input("Please choose between [1] Destruct or [2] Construct:\t"))

    if userInput == 1:
        alternade = input("Please Enter an Alternade: ")
        hasNumbers = any(char.isdigit() for char in alternade)

        if hasNumbers == True:
            print("Please Enter an Alternade without Numbers")
            break

        destruct(alternade)
    elif userInput == 2:
        wordOne = input("Please Enter Your First Word: ")
        hasNumbers = any(char.isdigit() for char in wordOne)

        if hasNumbers == True:
            print("Please Enter a Word without Numbers")
            break

        lengthOne = len(wordOne)
        wordTwo = input("Please Enter Your Second Word: ")
        hasNumbers = any(char.isdigit() for char in wordTwo)

        if hasNumbers == True:
            print("Please Enter a Word without Numbers")
            break

        lengthTwo = len(wordTwo)

        wordLength = lengthOne + lengthTwo
        construct(wordOne, wordTwo, wordLength)

    else:
        print("Please Enter a Valid Option: ")
        continue
