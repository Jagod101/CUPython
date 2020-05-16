# Assignment 7 - List and Tuples
```
Zach Jagoda
Student ID: 2274813
Student Email: jagod101@mail.chapman.edu
CPSC230
Assignment 7 - List and Tuples
```
```
Source Files: calculations.py, README.md
Errors: N/A
References: N/A
```
Program Descriptions:
```
Write a program that continually prompts the user for positive integer values and stores
them in a list. You should stop prompting when the user enters a negative integer value.
When the user is done entering values, you should print the list of integers they have
provided in sorted order. You should then compute the mean and standard deviation of the
values in the list.

Recall that the mean is just the arithmetic average...the sum of all the values divided by the
number of values. In mathematics notation we represent the mean with the Greek letter
mu, μ.

In statistics, standard deviation is the square root of variance and measures how much, on
average, values deviate from the mean. So consider a list of N numbers, with mean mu, μ :
Variance = σ^2 = Σ(Ni −μ)/N where Ni is the value at position i in the list.
Standard Deviation = σ = √σ2 = √V ariance

You should not be using any built in modules that calculate variance/standard deviation for
you, you need to code this on your own. In order to make your program as modular as possible, however, you should define your
own functions to carry out the computation. These functions should be:
● print_sorted – takes a list of integers as input and prints them in sorted order
● compute_mean – takes a list of integers as input and returns the mean (average) of
the list
● compute_variance – takes a list of integers as input and returns the variance of the
list. (Note that this method can call the computeMean method.)
● compute_standard_dev – takes the variance as input and returns the standard
deviation (just the square root of variance).

```
