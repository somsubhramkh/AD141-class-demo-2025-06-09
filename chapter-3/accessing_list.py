#!/usr/bin/env python3

# index starts with zero i.e. my_list[0] = "a" etc.
my_list = ["a","b","c","d","e","f"]


# accessing individual elements

print("First element:",my_list[0])
print("Third element:",my_list[2])
print("Last element:",my_list[5],my_list[-1])
print("Second Last element:",my_list[-2])

# Slicing


print("from index 1 to 3:",my_list[1:4])
print("from beginning to 3:",my_list[:4])
print("from index 3 to end:",my_list[3:])
print("all elements:",my_list[:])
print("every second elements:",my_list[::2])
print("reversed lists:",my_list[::-1])