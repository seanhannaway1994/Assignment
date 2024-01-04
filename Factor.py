"""
Author:             Sean Hannaway
SRN:                22039359
Date:               January 2024
Question:           Write a Python programme implementing the factorial of a positive integer n in recursive form.
                    Your program has to implement the following steps:
Description:        This program takes a user inputted Int (if the Int is a negative it, it will ask for another Int) and
                    computes the factorial of that Int, while printing the result and the current value of n throughout
                    the iterations.
"""

while True:
    n = int(input("Please Enter A Positive Int: "))

    if n >= 0:
        break  # Exit the loop if a positive or 0 integer is entered
    else:
        print(
            "No Positive Int Entered, Please Enter A Positive Integer And Try again.")  # Enter again until a positive Int is entered

def factor(n):
    if n == 0 or n == 1:  # if the user enters 1 or 0 then return the output as 1
        return 1
    else:
        return n * factor(n - 1)  # if not 1 or 2. Calculate n * n in a recursive form, decreasing n at every recursion


for i in range(n, 0,
               -1):  # range of values, starting at whatever the user inputs to 1, with a step size of -1 (reverse order) throught the iterations
    print(f"Current Value Of n: {i}")  # prints the current value of n after every iteration

# prints the calculation of n using the factor function
print(f"The Calculation of The Factorial of {n} is {factor(n)}")
