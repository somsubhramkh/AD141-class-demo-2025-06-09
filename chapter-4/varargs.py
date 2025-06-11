#!/usr/bin/env python3

def calculate_sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(calculate_sum(10,20,30))
print(calculate_sum(10,20,30,40,50))
print(calculate_sum())