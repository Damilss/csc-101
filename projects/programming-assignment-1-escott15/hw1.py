from cmath import phase

import data
import math

# Write your functions for each part in the space below.

# Part 1
"""

Purpose: The purpose of this function is to count the amount of vowels in a string
input type: str
output type:int
input example:cat
output example:1
How would I solve this if I were a computer? 
Define function (str) -> int:
-> def vowel count
After that I would create a instance variable which is a coutn
count = 0
Next I would create a list out of the string 
-> list()
After that I would create a loop going through each item in the list and comparing it to a set parameter
-> for loop 
If one of the letters matches a vowel, it wil add one to the count 
-> count+=1
then after that I would return count
->return count

"""

def vowel_count (x:str) -> int:
    vowels = 0
    n = list(x)
    for i in n:
        if i in 'aeiouAEIOU':
            vowels+=1
    return vowels

def main1():
    word_catalog = ["cat","dog","super", "great"]
    for i in word_catalog:
        print(vowel_count(i))

#Main1()
# Part 2
"""

Purpose: The purpose of this function is to find any nested lists within a bigger list that are equal to the length of 2,
and put them in a new list. 
input type: list[list[int]]
output type: list[list[int]]
input example: [[2, 3], [4, 5], [5, 7, 8, 9],[1]]
output example: [[2, 3], [4, 5]]
How would I solve this if I were a computer? define function 
-> def short_lists
Next I would create a list to put the new elements in. 
-> n = []
After, create loop to go through each element in the list and compare it to a set parameter
-> for loop 
-> if len(i) == 2: 
if true, append to new list 
n.append(i)
then return the finalized list 
return n 

"""

def short_lists (x: list[list[int]]) -> list[int]:
    n = []
    for i in x:
        if len(i) == 2:
            n.append(i)
    return n

def main2():
    number_list=[[3, 4], [5, 6], [7, 8, 9]]
    new_list = short_lists(number_list)
    print(new_list)
#main2()

# Part 3
"""

Purpose: Purpose of this function is to take a parameter type, and return a new list 
input type: list[list[int]]
output type: list[int] 
input example:[[5, 4], [67, 45, 23], [10, 0], [4]]
output example:[[4, 5], [67, 45, 23], [0, 10]]
How would I solve this if I were a computer? 

"""

def ascending_pairs (x:list[list[int]]) -> list[list[int]]:
    n = []
    for i in x:
        if len(i) == 2:
            if i[0] > i[1]:
                ph = i[1]   #placeholder
                i[1] = i[0]
                i[0] = ph
        n.append(i)
    return n

def main3():
    t = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 4], [7, 6],[11,10]]
    print(ascending_pairs(t))

#main3()


# Part 4
"""

Purpose: The purpose of this function is to add the class of 'price' to act as price of items.
input type:[Price (dollars, cents), Price (dollars, cents)]
output type: Price(dollars, cents)
input example:[Price(59,99), Price(59,99)]
output example:Price(119,98) 
How would I solve this if I were a computer? 
I created a dunder method for add to make the process of adding prices together a lot simpler
-> __add__ in data.py
define function 
-> def add_prices 
create a new list
-> n = [] 
create a for loop to go through items in the list and add them together. 
-> for loop
create a conditional statement to check if the user only added two prices together. 
-> if else statement
return 
"""
def add_prices(x:list[data.Price]) -> list[data.Price] or data.Price:
    n = []
    for i in range(0, len(x), 2):
        n.append(x[i] + x[i+1])
    if len(n) == 1:
        return n[0]
    else:
        return n



# Part 5
"""

Purpose: To find the area of a Rectangle object 
input type: data.Rectangle  
output type: float
input example: Rectangle(Point(0,0), Point(4,4))
output example: float(16.0) 
How would I solve this if I were a computer? 
define a function 
-> def rectangle_area 
Next I would create two variables for length and height and use the points to to get the length and height, then multiply
them by each other. 
l =
h = 

"""

def rectangle_area(rect: data.Rectangle) -> float:
    return (rect.bottom_right.x - rect.top_left.x) * (rect.bottom_right.y - rect.top_left.y)



# Part 6
"""

Purpose: The purpose of this function is to return all of the books made by an author when the name of the Author is given
input type: list[str, list[Book]]
output type:list[Book.title]
input example: ["James Patterson",
[Book(["Patterson", "James"],"1st to Die"),
 Book(["Patterson", "James"], "5th Horseman"),
  Book(["King","Stephen"], "It")]
  ] 
output example:["1st to Die", "5th Horseman"]
How would I solve this if I were a computer? 
define function
-> def books_by_author(list[Book]) -> list[str]:
I would assign a new variable to a list
-> n=[]
I would take the name of the Author inputted and create it into a matching list that is in the catalogs
-> Ex. Inputted name = "James Patterson", turn into -> ["Patterson", "James"] 
Next I would make for loop for each item in list of input
-> for loop!
the for loop would go through each individual item and check the authors to then append valid books into the new list
-> if x == Book.authors
return the new list created 
-> return n 
"""

def books_by_author(auth:str, book_catalog:list[data.Book]) -> list[str]:
    n = []
    auth_l = list(auth.split(" ")) #author input is getting turned into a list and the names are getting flipped to catalog
    ph = auth_l[0] #placeholder
    auth_l[0] = auth_l[1]
    auth_l[1] = ph
    for book in book_catalog:
        if book.authors == auth_l:
            n.append(book.title)
    print("books by", ", ".join(auth_l), "in catalog", n)
    return n
def main6():
    books = [
        data.Book(["Patterson", "James"], "1st to Die"),
        data.Book(["Patterson", "James"], "5th Horseman"),
        data.Book(["King", "Stephen"], "It"),
        data.Book(["King", "Stephen"], "The Shining"),
        data.Book(["Rowling", "J.K."], "Harry Potter and the Philosopher's Stone"),
        data.Book(["Rowling", "J.K."], "Harry Potter and the Chamber of Secrets"),
        data.Book(["Tolkien", "J.R.R."], "The Hobbit"),
        data.Book(["Tolkien", "J.R.R."], "The Lord of the Rings"),
        data.Book(["Christie", "Agatha"], "Murder on the Orient Express"),
        data.Book(["Christie", "Agatha"], "And Then There Were None"),
        data.Book(["Martin", "George R.R."], "A Game of Thrones"),
        data.Book(["Martin", "George R.R."], "A Clash of Kings"),
        data.Book(["Collins", "Suzanne"], "The Hunger Games"),
        data.Book(["Collins", "Suzanne"], "Catching Fire"),
        data.Book(["Brown", "Dan"], "The Da Vinci Code"),
        data.Book(["Brown", "Dan"], "Angels & Demons"),
        data.Book(["Atwood", "Margaret"], "The Handmaid's Tale"),
        data.Book(["Orwell", "George"], "1984"),
        data.Book(["Orwell", "George"], "Animal Farm"),
        data.Book(["Shelley", "Mary"], "Frankenstein"),
    ]
    search = "James Patterson"
    books_by_author(search, books)
if __name__ == "__main__":
    main6()


# Part 7
"""

Purpose: The purpose of this function is to find the smallest circle that can go around a rectangle with the smallest
possible circle.
input type: data.Rectangle
output type:data.Circle  
input example: data.Rectangle(data.Point(2, 8), data.Point(4, 8))
output example: data.Circle(data.Point(5,5), center(4.242640687119285))
How would I solve this if I were a computer?
I would first start with getting the midpoint with each diagonal point. So that we can get the center point for the 
circle.
-> (rect.top_left.x + rect.bottom_right.x) / 2
With this being said, now we can use the points of each given input points, (rect.top_left.x and rect.bottom_right.x)
we can get the distance between those two points we can get the 

dx = rect.bottom_right.x - rect.top_left.x


"""
def circle_bound(rect: data.Rectangle) -> data.Circle:
    # midpoint of diagonal
    cx = (rect.top_left.x + rect.bottom_right.x) / 2
    cy = (rect.top_left.y + rect.bottom_right.y) / 2

    # half of diagonal length
    dx = rect.bottom_right.x - rect.top_left.x
    dy = rect.bottom_right.y - rect.top_left.y
    radius = math.hypot(dx, dy) / 2

    return data.Circle(data.Point(cx, cy), radius)







# Part 8
"""
Purpose: The purpose of this function is to check which employees are being have 

Input type: list[Employee]

Output type: list[str]

Input example:[data.Price(Jack, 17.50), data.Price(Bernard, 35.00)]

output example:[Jack]

How would I solve this if I were a computer?: I would define the function 
-> def below_pay_average
Create a new list in the function to put the names of the employees are below the average pay rate. 
-> n =[]
Create for loop to go through each Employee
-> for loop
I would take each item in the list and check how much they are getting paid 
-> if statement
append each person in the input list to the new list 
-> n.append()
return the new list of with all the names of the people who are getting paid less
return n 

"""

def below_pay_average (x:list[data.Employee])-> list[str]:
    n = []
    pay_avg = 0
    ph =[]
    for i in x:
        ph.append(i.pay_rate)
    pay_avg = sum(ph)/len(ph)
    for i in x:
        if i.pay_rate <= pay_avg:
            n.append(i.name)
    return n