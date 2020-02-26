#Zach Jagoda and Daniel Kavesh
#Student ID: 2274813 and 2314750
#Student Email: jagod101@mail.chapman.edu and kavesh@chapman.edu
#CPSC230
#Assignment 3 - Part 2

#Write a program that prompts for an integer — let’s call it x — and then finds
#the sum of x consecutive integers starting at 1. That is, if x = 5, you will find the sum of 1 + 2
#+ 3 + 4 + 5 = 15.

#Declare the Variables
x = 0
sum = 0

#Prompt user for Consecutive Number Input
x = int(input("Enter a Number to Consecutive Sum - "))

#Iterate x times based on the input value
for i in range(x):
    #add the x variable to the sum
    sum = sum + x
    #decrease the x variable by 1 to create consecutive numbers
    x = x - 1

#Print the total Consecutive Sum
print("The Consecutive Sum is ", sum)
