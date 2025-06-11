#!/usr/bin/env python3

def outer_function(message):
    def inner_function():
        print(message)
    return inner_function

my_var = outer_function("Hello")
# my_var()
