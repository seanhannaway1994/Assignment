"""
Author:             Sean Hannaway
SRN:                22039359
Date:               January 2024
Description:        This program sorts the strings entered manually by the user into accesding order based on their
                    length and prints out the results, along with how many cities were ordered, the number of steps, swaps
                    and rounds it took to order the list. This program is a bubble sort algorithm.
"""
# Ask the user for input, strings are split into substrings using commas
cities = input("Enter Your List Of Cities Separated By Commas Please: ").split(',')

# Initialize loop variables
i = 0
swaps = True
number_of_cities = len(cities)
number_of_steps = 0
number_of_swaps = 0
number_of_rounds = 0

# Sort using bubble sort
while swaps:
    swaps = False
    number_of_rounds += 1
    for i in range(0, number_of_cities - 1):
        if len(cities[i]) > len(cities[i + 1]):
            temp = cities[i + 1]
            cities[i + 1] = cities[i]
            cities[i] = temp
            swaps = True
            number_of_swaps += 1
    number_of_steps += 1

# Output the result
print("The ordered list is:", cities)
print("The list had", number_of_cities, "cities and I ordered it in", number_of_steps, "steps.")
print("I did", number_of_swaps, "swaps in", number_of_rounds, "rounds.")
