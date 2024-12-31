#Doc strings in python are a simple description of the function.
#They are written in triple quotes.

def add(a, b):
    '''This function adds two numbers'''
    return a + b
#unlike comments, doc strings are stored in the __doc__ attribute of the function. We can print them with the help of the __doc__ attribute.
print(add.__doc__)
print(add(2, 3))

#Doc strings will be printed only if we add the string just below the function definition.

def pro(a, b):
    return a * b
'''This function multiplies two numbers'''

print(pro.__doc__)
#output: None 

#PEP 8
# The PEP 8 is a style guide for python code. It is a set of rules that specify how to format the code for maximum readability.
# It is recommended to follow the PEP 8 style guide while writing python code.
# The PEP 8 style guide can be found at https://www.python.org/dev/peps/pep-0008/

# Zen of Python
# The Zen of Python is a collection of 19 aphorisms that capture the philosophy of Python. It is written by Tim Peters.
# The Zen of Python can be accessed by typing import this in the python shell.
 