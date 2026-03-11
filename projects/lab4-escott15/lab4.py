from sys import prefix

import data

import math

# Write your functions for each part in the space below.

# Part 1
"""
Purpose: The purpose of this function is to take a list of nested integer and lists and create a new list with all of 
the first elements of each list.
input type: list1a[list2a[int], list2b[int]. list2c[int]
output type: newList[int(list2a[0]), int(list2b[0]), int(list2c[0])]
Example Input:a = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
Example Output: new = [1, 1, 1] 
How would I solve the problem if I was a computer?:
Create a function definition for the function and have in input of a, which is a list of list of integers 
-> def first_element (a:list[list[int]]) -> list[int]:
Create a new list to hold the values of the first element of each list of each list 
then for loop to go through each element in the list. -> for i in a 
create an if statement that checks if that element in the list is an integer, use isinstance to check if int. 
-> if isinstance (i[0], int): 
then return the new list with all of of the first integers of each list of the original list. 
-> return first_elements 


"""
def first_element (a: list[list[int]])-> list[int]:
    first_elements = []
    for i in a:
        if isinstance(i[0], int):
            first_elements.append(i[0])
    return first_elements
def main():
    a = [[3, 9, 97, 2, 4], [43, 5, 7, 0, 12, 2], [4, 53, 45, 67, 87, 2], [2, 5, 6, 7], [9, 54]]
    result1 = first_element(a)
    print(result1)

#main()



# Part 2
"""
Purpose:The purpose of this function is to take a list of points in Class 
point and to find the x value of each point, and put those values into 
it's own list. 
input type: list[data.Point]
output type:list[float]
Example Input:[Point(3, 5), Point(4, 6)]
Example Output:[3, 4]
How would I solve the problem if I was a computer?:
Define a function -> x_coordinates (p:list[data.Point(s)]) -> list [float]:
Then create a new list for the x points to go into
-> x_values = [] 
Then create a loop for each item in the given original list, to go through them and pull the x values out of each oen

"""
def x_coordinates (p:list[data.Point]) -> list[float]:
    x_values=[]
    for i in p:
        x_values.append(i.x)
    return x_values

def main1():
    home = data.Point(4, 2)
    store = data.Point(2, 2)
    work = data.Point(1, 1)
    locations  = [home, store, work]
    result1 = x_coordinates(locations)
    print(result1)


#main1()

# Part 3
"""
Purpose: The purpose of the function is to check if the point is in a positive quadrant. 
input type: list[data.Point]
output type: list[data.Point] 
Example Input:[(5, 0), (-4, 6), (-4, -1)]
Example Output: [(5, 0)] 
How would I solve the problem if I was a computer?: I would first create a function 
-> def are_in_positive_quadrant 
Create a new list for the data.Point values to go into 
newList = []
Next I create a for loop to go through all of the elements within the list ( For Loop)
-> for i in p: 
Next I check if the 


"""
def are_in_positive_quadrant (p:list[data.Point]) -> list[data.Point]:
    newlist = []
    for i in p:
        if isinstance(i, data.Point):
            if i.x >= 0:
                if i.y >= 0:
                    newlist.append(i)
        else:
            exit()
    return newlist

def main2():
    home = data.Point(4, 2)
    store = data.Point(-2, 2)
    work = data.Point(1, -3)
    obunga = data.Point(-3, -2)
    walmart = data.Point(1, 1)
    locations = [home, store, work, obunga ]
    result2 = are_in_positive_quadrant(locations)
    print(result2)

#main2()







# Part 4
"""
Purpose: To check the distance between two points and takes two parameters of data.Point and return the  Euclidian 
distance between
 them. 
input type: list[data.Point]
output type: int, distance 
Example Input: [Point (0, 0), Point (0, 1)]
Example Output: 1
How would I solve the problem if I was a computer?: First I would define a function 
-> def eudistance(point1, point2):
next I would get the numbers and make sure that they are integers, 
 -> (conditional statement) if isinstance (point1, data.Point) and isinstance (point2, data.Point):
 Next I would use the distance funciton in order to get the Euclidian distance between the two, then return it. 
 -> return math.dist(point1, point2)




"""
def eudistance (a:data.Point, b: data.Point)-> float:
     point1 = [a.x, a.y]
     point2 = [b.x, b.y]
     return math.dist(point1, point2)





def main3():
    home = data.Point(4, 2)
    store = data.Point(-2, 2)
    print(eudistance(home, store))


#main3()

# Part 5
"""
Purpose: The point of the function is to find the manhattan distance of the graphs 
input type:data.Point, data.Point
output type: int
Example Input:data.Point(0,0), data.Point(0,4)
Example Output: 2
How would I solve the problem if I was a computer?: The first thing that I would do is import math
-> import math
Next I would define a function: 
-> def manhattandistance(point1, point2):
next I would use the abs function and sum to get the manhattan distance 
then I would return the int that is produced from the function 
-> return int 


"""

def manhattandistance (a:data.Point, b:data.Point)-> int:
    result = abs(int(b.x) - int(a.x)) + abs(int(b.y) - int(a.y))
    return result
def main4():
    home = data.Point(4, 2)
    store = data.Point(-2, 2)
    result7 = manhattandistance(home, store)
    print(result7)




# Part 6
"""
Purpose: The purpose of this function is to find the distance between a point in a list and 0, for every point in the 
list
input type: list[data.Point]
output type: list[int]
Example Input:[data.Point(4,5), data.Point(6,0)]
Example Output: [6.40312, 6]
How would I solve the problem if I was a computer?:
The first thing that I would do is import math so that I have a more efficient way of solving for distance of each point
-> import math
The next thing that I would do is use the euclidian distance formula that I already have an plug it into this function, 
-> eudistance(data.Point(x1, y1), data.Point(x2, y2))
I would take that function that we have and put it in a for loop, and have the second data.Point in the eudistance be 
(0,0)
-> for loop! 
next just return the list of int
->list[int]


"""
def d (l:list[data.Point]) -> list[int]:
    origin = data.Point(0, 0)
    d_result = []
    for i in l:
        d_result.append(eudistance(i, origin))
    return d_result
def main5():
    favorites = [data.Point(6, 7), data.Point(8, 9), data.Point(10, 11), data.Point(11, 12)]
    d_favorites = d(favorites)
    print(d_favorites)
#main5()
