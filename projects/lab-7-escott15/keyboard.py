from convert import str_to_float
#task 2
#gather_numbers
"""
The purpose of this function is to gather numbers inputted by the user and return them in a list[float], then exits the
loop to enter
input type: None
output type: list[float] 
"""
def gather_numbers()->list[float]:
    result = []
    print("Gathering numbers to create a list...")
    while True:
        user_input = input("Enter a number or enter Done: ")
        if user_input == "done" or user_input == "Done":
            break
        result.append(str_to_float(user_input))
    return result

if __name__ == "__main__":
    gather_numbers()