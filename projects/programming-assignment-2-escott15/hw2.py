import data
import math
# Write your functions for each part in the space below.
# Part 1
"""
Purpose:The purpose of this function is to use two points to create a rectangle
input type: data.Point, data.Point
output type: data.Rectangle
input example: data.Point(0, 10), data.Point(20, 0)
output example: data.Rectangle (data.Point(0, 10), data.Point(20, 0))
How would I solve this if I were a computer?:
on define function 
-> def create function 
use if statement to check if bottom right x is less than top left x or if top left y is less than bottom right y 
-> if statement
if any statements above are true, flip the two points so that it makes a valid rectangle
-> top_left, bottom_right = bottom_right, top_left
return data.Rectangle (data.Point(0, 10), data.Point(20, 0)
"""
def create_rectangle(top_left: data.Point, bottom_right: data.Point):
    if bottom_right.x < top_left.x or top_left.y < bottom_right.y:
        top_left, bottom_right = bottom_right, top_left
    return data.Rectangle(top_left, bottom_right)

# Part 2
"""
Purpose: the purpose of this function to check if the first parameter of duration is shorter than the second 
parameter of Duration 
input type: data.Duration, data.Duration 
output type: boolean
input example: data.Duration(40, 45), data.Duration( 50,50)
output example: False
How would I solve this if I were a computer?: define function 
-> def create function 
check if d1 minutes are bigger than d2 minutes 
-> if statement
if true, then return false
-> return False 
if the minutes are equal, check if the d1 seconds are more than d2 seconds
-if statement
if true then return false
->return False
Then return True,  if it didn't enter the if statement
-> return True
"""
def shorter_duration_than(d1:data.Duration, d2: data.Duration) -> bool:
    if d1.minutes > d2.minutes:
        return False
    elif d1.minutes == d2.minutes:
        if d1.seconds > d2.seconds or d1.seconds == d2.seconds:
            return False
    return True

# Part 3
"""
Purpose: The purpose of this function is to check if a song is shorter than an upper bound parameter type Duration
input type: list [data.Song], data.Duration
output type: list[data.Song]
input example: [
data.Song("Drake", "Hotline Bling", data.Duration(4, 27)),
 data.Song("Drake", "Company", data.Duration(4, 13)),
 data.Song("Jden Ray", "fivethirty", data.Duration(1, 39)),
]
Output Example:[
data.Song("Jden Ray", "fivethirty", data.Duration(1, 39))
]
How would I solve this if I were a computer?:
define function 
-> def create function 
set a new list for the result. 
-> result 
create a for loop to go through each item in the list
-> for loop
Conditional statement to check for each item in the list if it is shorter than the duration given
-> if statement
append each song that is shorter than the upper bound to the result list
-> result.append(i)
then return the final list 
return result
"""
def songs_shorter_than(lst: list[data.Song], bound: data.Duration) -> list[data.Song]:
    result = []
    for i in lst:
        if shorter_duration_than(i.duration, bound):
            result.append(i)
    if result == []:
        return None
    return result

# Part 4
"""
Purpose: The purpose of this function is to return the durations of all of the songs added up one of the paramters 
which is list[song], but only up to the index up to the specified amount (list[4]). which is the next and last parameter 
type in the list. 
input type, list[data.Song], int
output type data.Duration
input example: [
data.Song("June Hymm", "Decemberists", data.Duration(4, 30),
data.Song("October", "Broken Bells", data.Duration(3:40),
data.Song("Dust in the Wind", "Kansas", data.Duration(3, 29),
data.Song("Airplanes", "Local Natives", data.Duration(3, 58)
]
Output Example: data.Duration(20,7)
How would I solve this if I were a computer?:
go to data.py and implement an __add__ to tweak the way that the duration class interacts with each other. Make it
so everything adds correctly.
-> (in data. py) def __add__ (self): 
define function
-> def create function 
set result equal to a duration object 
-> result = data.Duration (0,0) 
create a for loop to go through each item in the 


"""
def running_time(lst: list[data.Song], playlist: list[int]) -> data.Duration:
    result = data.Duration(0,0)
    for i in playlist:
        result += lst[i-1].duration
    return result

# Part 5
city_links = [
    # Central Coast
    ['san luis obispo', 'santa margarita'],
    ['san luis obispo', 'pismo beach'],
    ['san luis obispo', 'morros bay'],
    ['santa margarita', 'atascadero'],
    ['atascadero', 'creston'],
    ['pismo beach', 'grover beach'],
    ['grover beach', 'arroyo grande'],
    ['arroyo grande', 'nipomo'],
    ['nipomo', 'santa maria'],
    ['santa maria', 'orcutt'],
    ['orcutt', 'los alamos'],
    ['los alamos', 'buellton'],
    ['buellton', 'solvang'],
    ['solvang', 'santa ynez'],
    ['santa ynez', 'los olivos'],
    ['los olivos', 'santa maria'],

    # Bay Area
    ['san francisco', 'oakland'],
    ['oakland', 'berkeley'],
    ['berkeley', 'richmond'],
    ['san francisco', 'san mateo'],
    ['san mateo', 'palo alto'],
    ['palo alto', 'san jose'],
    ['san jose', 'santa clara'],
    ['santa clara', 'milpitas'],
    ['milpitas', 'fremont'],
    ['fremont', 'hayward'],
    ['hayward', 'oakland'],

    # Southern California
    ['los angeles', 'glendale'],
    ['glendale', 'pasadena'],
    ['pasadena', 'arcadia'],
    ['los angeles', 'long beach'],
    ['long beach', 'seal beach'],
    ['seal beach', 'huntington beach'],
    ['huntington beach', 'newport beach'],
    ['newport beach', 'irvine'],
    ['irvine', 'lake forest'],
    ['lake forest', 'mission viejo'],
    ['mission viejo', 'san juan capistrano'],
    ['san juan capistrano', 'dana point'],
    ['dana point', 'san clemente'],

    # Inland
    ['bakersfield', 'tehachapi'],
    ['tehachapi', 'mojave'],
    ['mojave', 'palmdale'],
    ['palmdale', 'lancaster'],
    ['lancaster', 'santa clarita'],
    ['santa clarita', 'los angeles'],
    ['bakersfield', 'wasco'],
    ['wasco', 'delano'],
    ['delano', 'tulare'],
    ['tulare', 'visalia'],
    ['visalia', 'hanford'],
    ['hanford', 'lemoore'],
    ['lemoore', 'coalinga'],
    ['coalinga', 'king city'],

    # Sierra Nevada / North
    ['fresno', 'madera'],
    ['madera', 'merced'],
    ['merced', 'modesto'],
    ['modesto', 'stockton'],
    ['stockton', 'sacramento'],
    ['sacramento', 'davis'],
    ['davis', 'fairfield'],
    ['fairfield', 'napa'],
    ['napa', 'santa rosa'],
    ['santa rosa', 'petaluma'],
    ['petaluma', 'novato'],
    ['novato', 'san rafael'],
    ['san rafael', 'san francisco'],
]
def validate_route (database:list[list[str]], route:list[str]) -> bool:
    if len(route) < 1:
        return False
    for i in range(len(route)-1):
        temp_list1 = list(route[i:i+2])
        temp_list2 = temp_list1[::-1]
        if temp_list1 not in database and temp_list2 not in database:
            return False
    return True

# Part 6
"""
Purpose: The point of the function is to find the longest repetition of a list of integers that are in ascending order 
input type: list[str]
output type: int or none
"""
def longest_repetition(lst:list[int]):
    starting_count = 0
    small_idx = 0
    if len(lst) < 1:
        return None
    for i in range(len(lst)):
        count = 0
        for j in lst:
            if j == lst[i]:
                count += 1
        if starting_count < count:
            starting_count = count
            small_idx = i
    return small_idx