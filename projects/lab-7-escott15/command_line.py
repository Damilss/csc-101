import sys
from convert import str_to_float

"""
The purpose of this script is to convert a string to float within the argument values placed into the command line 
parameters
input type: sys.argv
"""
if __name__ == '__main__':
    print(sys.argv)
    result = 0.0
    for i in sys.argv[1:]:
        if i is not None:
            result += str_to_float(i)

    print (result)