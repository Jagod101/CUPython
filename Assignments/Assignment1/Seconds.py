#Zach Jagoda
#Student ID: 2274813
#Student Email: jagod101@mail.chapman.edu
#CPSC230
#Assignment 1 - Part 4

### A day has 86,400 seconds (24*60*60).
### The program should prompt the user for a number in range 1 to 86,400 and output the current time as hours, minutes, and seconds with a 24-hour clock.
### For example: 70,000 seconds is 19 hours, 26 minutes, and 40 seconds.

#Declare variables used in program
range = 0.0
hours = 0.0
minutes = 0.0
seconds = 0.0

#Input Range of Seconds to convert
range = float(input("The number you enter will be printed as hours, minutes and seconds. Please enter a number between the range 1 to 86,400: "))

#Calculate Hours
seconds = range % (24 * 3600)
hours = seconds // 3600
#Calculate Minutes
seconds = range % 3600
minutes = seconds // 60
#Calculate Seconds
seconds = range % 60

#Print Results
print("You entered ", range, " seconds which is ", round(hours, 1), " hours, ", round(minutes, 1), " minutes, and ", round(seconds, 2), " seconds")
