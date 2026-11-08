n: int = 5  # we declare n as int

name: str = "Harry"   # we declare name as string 


def sum(a: int, b: int) -> int:    # we declare this function is taking 
     return a + b                  # input of 2 int and returning the int value



from typing import List, Tuple, Dict, Union

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"
identifier = 12345  # Also valid


#Ye sab type hints hain. Matlab Python ko aur programmer ko bataya ja raha hai ke kis
 #  variable mein kis type ka data expected hai.