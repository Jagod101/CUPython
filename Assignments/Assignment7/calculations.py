#Zach Jagoda
#Student ID: 2274813
#Student Email: jagod101@mail.chapman.edu
#CPSC230
#Assignment 7 - Lists and Tuples

negativeValue = False                                   #Delcare a Boolean for the While Loop
intList = []                                            #Create an Empty List

def print_sorted(intList):                              #Function to Print a Sorted List
    intList.sort(key = float)
    print("Sorted List: ", intList)

    return intList

def compute_mean(intList):                              #Function to Compute the Mean of the List
    mean = sum(intList)/len(intList)
    print("Mean of the List: ", mean)
    return mean

def compute_variance(intList):                          #Function to Compute the Variance of the List
    mean = compute_mean(intList)
    variance = sum((x - mean) ** 2 for x in intList)/len(intList)
    print("Variance of the List: ", variance)
    return variance

def compute_standard_dev(variance):                     #Function to Compute the Standard Deviation of the List
    standard_dev = variance ** 0.5
    print("Standard Deviation of the List: ", standard_dev)
    return standard_dev

while negativeValue == False:                           #While Loop taking Positive Integers for Input until a Negative Value appears
    intHold = float(input("Please Enter an Integer: "))

    if intHold > 0:
        intList.append(intHold)
    elif intHold < 0:
        negativeValue = True
        break

intList = print_sorted(intList)
variance = compute_variance(intList)
standard_dev = compute_standard_dev(variance)
