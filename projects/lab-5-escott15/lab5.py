import data
import math
# Write your functions for each part in the space below.
# Part 1
   # The function for Part 1 should be within the class in data.py.
# Part 2
   # The function for Part 2 should be within the class in data.py.
# Part 3
"""
Purpose: The purpose of this function is to able to add time together.
Input type:(data.Time, Data.Time)
Output type:data.Time 
Input Example:(data.Time(4:20:45), data.Time(4:20:45)
Output Example:data.Time(8:41:30)
How would I solve this If I were a computer?:
Define function 
-> def time_add
Next I would find add everything together
-> time1.hour + time2.hour
-> time1.minute + time2.minute
-> time1.second + time2.second
and after that I would carry over what gets over flowed (I.E if there the sum of time1.second and time2. seconds 
is 67, then I would have to move the 60 over to the minute 
-> divmod(time_sum.second, 60)
return the sum of everything
-> time_sum
"""
def time_add(time1, time2):
    result = data.Time(
        time1.hour + time2.hour,
        time1.minute + time2.minute,
        time1.second + time2.second
    )
    if result.second >= 60:
        ph1 = divmod(result.second, 60) #placeholder 1
        result.second = ph1[1]
        result.minute += ph1[0]
    if result.minute >= 60:
        ph2 = divmod(result.minute, 60) #placeholder 2
        result.minute = ph2[1]
        result.hour += ph2[0]
    return result
# Part 4
"""
Purpose: The purpose of this function is to take a list of floats and to return true if all of the float values are 
strictly descending as the list progesses
input type: list[float]
output type: bool
input example: list[5.0, 4.0, 3.0, 2.0]
output example: True
How would I solve this if I were a computer?: define function 
->def is_descending
Set and name a variable and set it to true
-> result = True
create a count variable and set it to 0 
-> count = 0 
Create a While loop to go through each item in the list making sure the first item is less than the previous
-> while loop
the count will go up as the while loop goes through each item in the list and it will be used as a counter for comparing 
each item in the list. within the while loop there wil be an if statement to check each time if the first element is less
than the previous.
-> if statement
Lastly it will return the result statement. 
->return result 
"""
def is_descending(x:list[float]) -> bool:
    result = True
    count = 0
    while result == True and count < len(x)-1:
        if x[count]>x[count+1]:
            count = count + 1
        elif x[count] ==x[count+1]:
            count = count + 1
        elif x[count]<x[count+1]:
            result = False
    return result
# Part 5
"""
Purpose: The purpose of this function is to take a a list, and two numbers, an upper limit, and a lower limit integer 
to find the biggest integer bound,
input type: int, int, list[int]
output type: int
input example: ([1, 5, 6, 8, 9, 10], 2, 9)
output example: 9
How would I solve this if I were a computer?:
"""
def largest_between(x: list[int], upper:int, lower:int) -> int:
    n=[]
    count = 0
    result = 0
    for i in x:
        if i in range(lower,upper):
            n.append(i)
    while count < len(n)-1:
        if n[count]< n[count+1]:
            result = n[count+1]
        count +=1
    if n == []:
        return None
    elif len(n) == 1:
        return n[0]
    else:
        return result
# Part 6
"""
Purpose: The purpose of this function is to find the further point in a list fo points from the origin 
input type: list[data.Point]
output type: data.Point
input example: [data.Point(2.0,4.0), data.Point(3.0,3.0), data.Point(45.0,0.0)]
output example: data.Point(45.0, 0.0)
How would I would solve this if I was a computer: 
"""
def furthest_from_origin(x:list[data.Point])-> data.Point:
    n=[]
    count = 0
    result = 0
    for i in x:
        point1 = [i.x,i.y]
        point2 = [0,0]
        n.append(math.dist(point1,point2))
    while count < len(n)-1:
        if n[count]< n[count+1]:
            result = count + 1
        count += 1
    if x:
        return x[result]
    elif not x:
        return None