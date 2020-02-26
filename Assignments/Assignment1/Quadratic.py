#Zach Jagoda
#Student ID: 2274813
#Student Email: jagod101@mail.chapman.edu
#CPSC230
#Assignment 1 - Part 3

### The program should prompt the user for the coefficients a, b, c of a quadratic function.
### The program should then calculate and display the roots of the function using the quadratic formula.
### For now, only use values that will return a positive discriminate, test a = -1, b = 2, c = 3, you should get x = -1 and x = 3 for answers.

#Import Math Library for Calculations
import math

#Declare Variables
a = 0.0
b = 0.0
c = 0.0
d = 0.0

#Ask for User Input
a = float(input("What is the Value of A: "))
b = float(input("What is the Value of B: "))
c = float(input("What is the Value of C: "))

#Calculate
d = (b ** 2) - (4 * a * c)

#Take the Square Root for both the Positive and Negative Value
x1 = (-b - math.sqrt(d))/(2 * a)
x2 = (-b + math.sqrt(d))/(2 * a)

#Print the Solution
print("The solution is x =", x1, " and x =", x2)
