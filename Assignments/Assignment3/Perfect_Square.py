#Zach Jagoda and Daniel Kavesh
#Student ID: 2274813 and 2314750
#Student Email: jagod101@mail.chapman.edu and kavesh@chapman.edu
#CPSC230
#Assignment 3 - Part 3

#Write a short program prompts the user for a number, print out
#whether the number is a perfect square, and prompts the user for another number if the
#number was not a perfect square.
#A perfect square is a number that has a whole number square root. For example, 25 is
#a perfect square, because 5, is a whole number.

#Import the Math Library
import math

#Declare the Variables
number = 0
root = 0
run = True

#Set Run = True so the while loop will repeat until a Perfect Square occurs
while run:
     #Prompt the User for a Number
     number = int(input("Enter a Number "))

     #Take the Square Root of the Number
     root = math.sqrt(number)

     #If the Root is equal to the Number
     if int(root + 0.5) ** 2 == number:
         #Print to Console
         print(number, "is a Perfect Square")
         #Set Run = False to stop the While Loop
         run = False
         #Break out of the Loop
         break
     #If the Root is not equal to the Number
     else:
         #Print to Console to Try Again
         print(number, "is not a Perfect Square. Try Again")
         #Continue the Loop
         continue
