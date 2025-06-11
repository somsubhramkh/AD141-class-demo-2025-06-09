#!/usr/bin/env python3

# defining the function

def greet(name):
    """
    this function will greet the person whose name is passed
    as a parameter
    """
    print("Hello",name)
    print("Have a good day")

# calling the function
greet("Som")
print(greet.__doc__)