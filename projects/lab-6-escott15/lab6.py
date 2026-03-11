import data
from typing import Optional

# Write your functions for each part in the space below.



# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
"""
Purpose: The purpose of this function is to sort the books alphabetically by title.
input type: list[data.Book]
output type: None
input example:
small_books = [
    Book("Zoo", "James Patterson", 2012),
    Book("Alpha", "Greg Rucka", 2010),
    Book("Delta", "Tony Park", 2018),
]
output example: None
How would I solve this if I were a computer?: define the function 
-> def function
Then I would implement selection sort. 
->def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp 
"""
def selection_sort_books(lst:list[data.Book]) -> None:
    if not lst:
        return
    for book in range(len(lst)-1):
        mindex = book
        for idx in range(book+1, len(lst)):
            if lst[idx].title < lst[mindex].title:
                mindex = idx
        if mindex != book:
            lst[book], lst[mindex] = lst[mindex], lst[book]





# Part 2
"""
purpose: two swap uppercase letters for lowercase letters and lowercase letters for uppercase letters
input type: str
output type: str 
input example: Pinapple
output example: pINAPPLE
How would I solve this if I were a computer?:
define function 
-> def function 
for loop to go through each letter in the string
-> for item in str
then use if else statements to organize accordingly. 
"""
def swap_case(text: str) -> str:
    result = ""
    for ch in text:
        if ch.islower():
            result += ch.upper()
        elif ch.isupper():
            result += ch.lower()
        else:
            result += ch
    return result

# Part 3
"""
Purpose: The purpose of this function is to translate one type of str character and translate it to a different type of
character within a certain string.
input type: 
output type:
How would I solve this if I were a computer?
I would first define a function: 
-> def function 
create a new variable to hold the place of the result:
-> result = ""
and then create a for loop to go through each character in the str
-> for item in str
then use conditional statements to check if each character needs to be replaced.
then return the new string:
-> return result
"""
def str_translate(text: str, old: str, new: str) -> str:
    result = ""
    for ch in text:
        if ch == old:
            result += new
        else:
            result += ch
    return result



# Part 4
"""
The Purpose: of this function is to record how many times a specific words can pop up within a specific string 
input type: str
output type: dict[str, int]
How would I solve this if I were a computer?
define the returning varaiable
 -> counts = {}
create a for loop to go through each item in the list and check it 
-> for loop
create conditional if else statements to check if the item has already been made or if it just needs to be added to an 
already made key
-> if else statement
Then return the dictionary from the function
-> return counts 
 
"""
def histogram(text: str) -> dict[str, int]:
    counts = {}
    for word in text.split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts