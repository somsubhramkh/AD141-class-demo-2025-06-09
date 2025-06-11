#!/usr/bin/env python3

def process(list_of_items):
    for item in list_of_items:
        print(item,end="\n")

fruits = ["banana","apple","strawberry"]
process(fruits)

numbers = (10,20,30)
process(numbers)