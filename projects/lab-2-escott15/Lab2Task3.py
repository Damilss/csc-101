
def smallest(n:float, m:float) -> float:
    if n < m:
        return n    # For which calls below is this statement evaluated?: Line 10, second = smallest (n:2 m:2)
    else:
        return m

first = smallest (3, 2)     #WHat is the value of first?: 2
second = smallest (2, 2)     #What is the value of second? Is this a reasonable result? Why or why not? value is 2
#it's reasonable, both integers are in there, but it is little confusing.
print()


# 2nd


def function2 (a:int, b:int, c:int) -> float:
    if a > b and a > c:
        return a - b    #In general, when will a call to this function evaluate this statement?: when a is greater than b and a greater than c
    elif b > c:
            return b + c    #In general, when will a call to this function evaluate this statement?: when b greater than c and not ( a > b and a > c)
    else :
        return 2 * c    #In general, when will a call to this function evaluate this statement?: when not (a > b and a > c) and b > c
answer1 = function2(3, 2, 1)    #What is the value of answer1?: answer: 1
answer2 = function2(2, 3, 1)    #What is the value of answer 2?: Answer: 4
answer3 = function2(2, 1, 3)    #What is the value of answer 3?: Answer: 6
print()
