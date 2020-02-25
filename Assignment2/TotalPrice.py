#Zach Jagoda and Daniel Kavesh
#Student ID: 2274813 and 2314750
#Student Email: jagod101@mail.chapman.edu and kavesh@chapman.edu
#CPSC230
#Assignment 1 - Part 1

###The program should find the total price of an item given the price and sales tax.
###The program should prompt the user for the purchase price of an item and the sales tax rate,
###it should display the total price of the item.
###The user should be able to enter values such as 10.25 for price and 7.5 for sales tax rate.

#Declare Variables
purchasePrice = 0.0
salesTax = 0.0
totalPrice = 0.0

#Prompt for User Input
purchasePrice = float(input("What was the Purchase Price of your Item: "))

#Check to see if purchasePrice is greater than 0, continue if it is...
if purchasePrice > 0:
    salesTax = float(input("What was the Sales Tax on your Item: "))
    
    #Check to see if the salesTax is greater than 0, continue if it is...
    if salesTax > 0:
        #Calculate the Total Price
        totalPrice = (purchasePrice * (salesTax/100)) + purchasePrice
        #Print the Results
        print("The Total Price for your Item is: ", round(totalPrice, 2))

    #...else, tell the user the number cannot be negative
    else:
        print("The Sales Tax shouldn't be negative")

#...else, tell the user the number cannot be negative
else:
    print("The Sales Price shouldn't be negative")
