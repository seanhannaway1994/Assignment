
"""
Author:             Sean Hannaway
SRN:                22039359
Date:               January 2024
Description:        This program sorts the strings entered manually by the user into accesding order based on their
                    length and prints out the results, along with how many cities were ordered.
                    This program is a quick sort algorithm. 

3.1 Sorting
2. Implementation
(c) Implement ONE sorting algorithm from the following list: merge sort, quick sort, selection
sort, insertion sort.
"""

# define the quick sort function
def quick_sort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[len(list) // 2] # pivot is the middle of the list inputted.
        left, middle, right = [], [], [] # create 3 empty lists left of the pivot, right and == pivot.
        for city in list: # for all the cities that take the arguement 'list'
            if len(city) < len(pivot): # elements < pivot, add to left list
                left.append(city)
            elif len(city) == len(pivot): # elements = pivot, add to middle list
                middle.append(city)
            else: #elements > pivot, add to right list
                right.append(city)
        return quick_sort(left) + middle + quick_sort(right) # concatenate the 3 lists


# Ask the user for input, strings are split into substrings using commas
cities = input("Enter Your List Of Cities Separated By Commas Please: ").split(',')

# output the result
print("The sorted list now looks like this in quick sort:", quick_sort(cities))
print("The list was", len(cities), "cities long")