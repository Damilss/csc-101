

from typing import Optional  #gain access to the optional [x] type hint


def checked_access(L: list[int], idx: int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)  #What is the value of test on each call?: on first, test = false
    if test:
        return L[idx]
    else:
        return None


first = checked_access([1, 0, 1], 9)  #What is the value of first?: None
second = checked_access([1, 0, 1], 2)  #What is the value of second?: 1
print()


#2nd
def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])   #For which call below is this statement evaluated line 30, first
    elif len(L) >1:     #What values are being added: the number of characters in each item of L [0], [1], [2]
        result = len(L[0]) + len(L[1])  #For which call below is this statement evaluated?: Lines 31 and 32, second and third
    elif len(L) >0:     #And what are the values being added?: the length of characters in L[0]
        result = len(L[0])     #For which call below is this statement evaluated?: There is no call for this statement
    else:   #And what are the values being added? No values are being added, result is simply being set to 0
        result = 0
    return result
first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum([ "second call"])
third = length_sum([ "another call"])
print()




#3rd

def suprising(L:list[str], other:str ) -> list[str]:
    L.append(other.upper())
    return L

words = ["this", "is", "confusing", "code"]
first = suprising(words, "avoid")
second = suprising(words, "such")
#What is the value of words at this point?: ['this', 'is', 'confusing', 'code', 'AVOID', 'SUCH']
#What are the values first and second at this point?: They are both ['this', 'is', 'confusing', 'code', 'AVOID', 'SUCH']
#What happened?: Since lists are mutable, they all changed when the list was appended in the function suprising.
print()