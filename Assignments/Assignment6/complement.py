#Zach Jagoda
#Student ID: 2274813
#Student Email: jagod101@mail.chapman.edu
#CPSC230
#Assignment 6 - Complement

#Define Program Function
def rev_complement():
    #Take DNA Sequence Input from User
    dnaInput = input("Please Input a DNA Sequence: ")
    #Make any Input Upper Case
    dnaSequence = dnaInput.upper()

    #Create the Complement of the DNA Sequence
    complemetSequence = ""
    for i in dnaSequence:
        if i == 'A':
            complemetSequence += 'T'
        elif i == 'T':
            complemetSequence += 'A'
        elif i == 'G':
            complemetSequence += 'C'
        elif i == 'C':
            complemetSequence += 'G'

    #Create the Reverse Complement of the Complement Sequence
    reversedSequence = complemetSequence[::-1]

    #Print all Three DNA Sequences
    print("Original Sequence: ", dnaSequence)
    print("Complement Sequence: ", complemetSequence)
    print("Reversed Complement Sequence: ", reversedSequence)

rev_complement();
