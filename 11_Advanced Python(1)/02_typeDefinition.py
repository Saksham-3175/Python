# Very important as this helps others understand your code well and helps you also.
#Some of the methods come without even using type definition but still it would be a good practice to use it.

n : int = 3
print(n.bit_length(), 'is the length of bits the variable n holds.')
#The bts is, when you say python that var 'n' is an integer by using ': dtype', it automatically gives you methods based on that particular dtype(int in this case) by n.(suggetions by python)

#Function definition with type hints
def add(a: int, b: float) -> float:
    return a + b
add(1, 3.3)

#The bts is, you can use type hints to define the type of arguments(:int and :float) and return type of the function(->). This helps when you are calling the function as it gives you suggestions based on the type hints you have given.

#For advanced type hints, you can use the typing module
from typing import List, Tuple, Dict, Any, Union, Optional

#Write the code.....
