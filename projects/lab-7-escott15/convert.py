
#task 1
#str_to_float
"""
The purpose of this function is to take the incoming parameter, which is a string, and then convert it to a float.
input type: string
output type: float
"""


def str_to_float(s: str) -> None | float:
    try:
        return float(s)
    except ValueError:
        return None