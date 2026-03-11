import sys
import pprint 
#DISCPLAIMER, this file handling Python script only works for CSV files, 


#From lab 7
#returns any input of function from string to float
#input: str
#output: float 
def str_to_float(s: str) -> None | float:
    try:
        return float(s)
    except ValueError:
        return None

_cmdarg = sys.argv[1] #Command line argument

#filehandling in order to get the contents out of the file.
try: 
    fileobj = open("{}".format(sys.argv[1]),"r")
except FileNotFoundError as _fnf:
    print("That is not a valid file name. Please enter a valid file name")
    exit()
_cmdargdata = fileobj.readlines()
fileobj.close()
_maindata = []
_invalidlines_idx = []
for _line in _cmdargdata: 
    _line = _line.strip("\n")
    temp = _line.split(",")
    _maindata.append(temp)

#Converting each string value within the main data into float to make it computable. 
for i in range(len(_maindata)):
    for j in range(len(_maindata[i])):
        temp = str_to_float(_maindata[i][j])
        if temp == None and j == 0: 
            print("Unable to caluclate, not a float value within line")
        elif temp == None and j==1 and not _maindata[i][0] == None: 
            print("Unable to calculate, not a float value within line")
        _maindata[i][j] = temp
    try: 
        if _maindata[i][0] == None or _maindata[i][1] == None:
            _invalidlines_idx.append(i)
    except IndexError as ie:
        _invalidlines_idx.append(i)
        

#To find the final sums of each two floats within each line.
result = {}
for i in range(len(_maindata)):
    if i not in _invalidlines_idx:
        if _maindata[i][0] != None and _maindata[i][1] != None:
            result["line {}".format(i)] = sum(_maindata[i])
    else:
        result["line {}".format(i)] = "Not calulacted (Value or index Error)"

if __name__ == "__main__":
    print(pprint.pformat(result, indent = 4))