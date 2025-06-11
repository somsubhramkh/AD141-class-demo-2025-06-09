#!/usr/bin/env python3

def add(a,b):
    return a+b


def subtract(a,b):
    return a-b


def perform_operation(fn,a,b):
    return fn(a,b)

print(perform_operation(add,10,2))
print(perform_operation(subtract,10,2))