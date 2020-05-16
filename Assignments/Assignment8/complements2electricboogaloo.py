#Zach Jagoda
#Student ID: 2274813
#Student Email: jagod101@mail.chapman.edu
#CPSC230
#Assignment 8

#Define the Program Function
def rev_complement():
    try:                                                            #Set a Try
        fileName = input('Please Input a File Name: ')              #Ask User for a File Name
        fileInput = open(fileName, 'r')                             #Open the File and set to Read
        fileOutput = open("results_complement.txt", 'w')            #Create an Output File and set to Write

        for x in fileInput:                                         #Create the DNA Sequence from the File
            dnaSequence = x.upper()

        fileInput.close()                                           #Close the Read File
        fileOutput.write("DNA Sequence: " + dnaSequence + "\n")     #Write the DNA Sequence to the Output File

        complemetSequence = ""                                      #Create the Complement Sequence from the DNA Sequence
        for i in dnaSequence:
            if i == 'A':
                complemetSequence += 'T'
            elif i == 'T':
                complemetSequence += 'A'
            elif i == 'G':
                complemetSequence += 'C'
            elif i == 'C':
                complemetSequence += 'G'

        fileOutput.write("Complement Sequence: " + complemetSequence + "\n")            #Write Complement to the Output File

        reversedSequence = complemetSequence[::-1]                                      #Create the Reversed Complement
        fileOutput.write("Reversed Complement Sequence: " + reversedSequence + "\n")    #Write the Reversed Complement to the Output File

        fileOutput.close()                                          #Close the Output File
    except:                                                         #Set the Except
        print("Invalid")                                            #If the Try Fails, alert the User

rev_complement();
