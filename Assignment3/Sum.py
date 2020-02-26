#Zach Jagoda and Daniel Kavesh
#Student ID: 2274813 and 2314750
#Student Email: jagod101@mail.chapman.edu and kavesh@chapman.edu
#CPSC230
#Assignment 3 - Part 1

#Write a python program that prompts the user for the how many numbers he/she
#would like to sum and then asks the user for each number and displays the sum.

#Declare the Variables
number = 0
totalSum = 0
iteration = 0

#Prompt the user for how many Iterations they want
iteration = int(input("How many numbers do you want to Sum? "))

#Iterate through the input variable
for i in range(iteration):
    #Prompt the user for a number for each iteration
    number = int(input("Enter a Number: "))
    #Add the input to the Total Sum
    totalSum = totalSum + number
    #Display the sum after adding the Input
    print("The Total Sum is ", totalSum)
