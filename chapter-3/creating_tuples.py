#!/usr/bin/env python3

# empty_tuple = ()
# print(empty_tuple,type(empty_tuple))

# my_tuple = (1,2,3,"Hi",10.3)
# print(my_tuple)

# single_element_tuple = (10,)
# print(type(single_element_tuple))

# # packing tuple

# my_tuple = 10,20,"apple"
# print(my_tuple, type(my_tuple))

# fruits = ("banana", "apple", "strawberry")

# # accessing a tuple
# print(fruits[0])
# print(fruits[2])
# print(fruits[0:2])
# print(fruits[-1])

# tuple is immutable, so you can't modify an element

# fruits[0] = "Kiwi"

# tuple concatenation
t1 = (1,3)
t2 = (2,4)

t3 = t1 + t2
print(t3)


# repetition
repeated_tuple = t1 * 3
print(repeated_tuple)

print(len(repeated_tuple))

print(1 in t3)

# iteration

fruits = ("banana", "apple", "strawberry")
for fruit in fruits:
    print(fruit)


# tuple unpacking

f1, f2, f3 = fruits
print(f1,f2)

a = 1
b = 2

a,b = b,a

print(a,b)

