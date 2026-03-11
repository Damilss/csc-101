

# to take a list of integers of any element and group them in groups of 3, returning group of three items in its own list wihtin the outer list
# input: list[int]
# output: list[list[int]]
def groupsof3 (lst:list[int]) -> list[list[int]]:
    newlst = []
    j = divmod(len(lst), 3)
    if j == (0, 0): 
        return newlst
    elif not isinstance(lst, list):
        print("not list, please enter list")
        return
    if j[0] > 0:
        for i in range(j[0]):
            newlst.append(lst[i*3:i*3+3])
    if j[1] > 0:
        newlst.append(lst[j[0]*3::])
    return newlst
    
