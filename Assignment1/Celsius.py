#Zach Jagoda
#Student ID: 2274813
#Student Email: jagod101@mail.chapman.edu
#CPSC230
#Assignment 1 - Part 2

### The program should prompt the user for the temperature in Celsius.
### It should then convert this temperature into Fahrenheit and display the temperature in Fahrenheit.

#Delcare Variables
celsius = 0.0
fahrenheit = 0.0

#Prompt for User Input
celsius = float(input("What is the Temperature in Celsius: "))

#Calculate the Temperature Conversion
fahrenheit = (celsius * (9/5)) + 32

#Print the Results
print("The Temperature in Fahrenheit is: ", fahrenheit)
