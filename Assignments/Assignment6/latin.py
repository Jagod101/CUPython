#Zach Jagoda
#Student ID: 2274813
#Student Email: jagod101@mail.chapman.edu
#CPSC230
#Assignment 6 - Latin

#Set the Pig Latin Variations
ay = "ay"
yay = "yay"
#Set What Are Consonants and Vowels
consonant = ("B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z")
vowel = ("A", "E", "I", "O", "U")

#Function for a Singular Word
def word_to_pig(word):
    firstLetter = word[0]                                   #Take the first letter of the word
    firstLetter = firstLetter.upper()                       #Make sure it is Upper Case with .upper()

    if firstLetter in consonant:                            #Check if the letter is a Consonant
        wordLength = len(word)
        removeFirst = word[1:wordLength]
        pigLatin = removeFirst + firstLetter.lower() + ay
        pigLatin = pigLatin.capitalize()
    elif firstLetter in vowel:                              #Check if the letter is a Vowel
        pigLatin = word + yay
        pigLatin = pigLatin.capitalize()
    else:                                                   #If it is not a Consonant or a Vowel...
        print("I don't recognize ", firstLetter)

    return pigLatin                                         #Return the Pig Latin Word

#Function for a Name (First and Last)
def name_to_pig(first_name, last_name):
    pigFirst = word_to_pig(first_name)                      #Send the First name to word_to_pig
    pigLast = word_to_pig(last_name)                        #Send the Last Name to word_to_pig

    print(first_name + " " + last_name, "becomes", pigFirst + " " + pigLast)    #Print the Results
    return

firstName, lastName = input("Please Enter Your Name: ").split() #Ask the User for their Name
name_to_pig(firstName, lastName)                                #Send the First and Last Name to name_to_pig
