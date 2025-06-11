#!/usr/bin/env python3

numbers_list = [1,2,3,4,5]

def square(n):
    return n*n

print(list(map(square,numbers_list)))


# filter

def find_even(n):
    return n%2 == 0

even_numbers = list(filter(find_even,numbers_list))
print(even_numbers)