#!/usr/bin/env python3

square = {x:x**2 for x in range(1,10)}
print(square)


keys = ["a","b","c"]
values = [10,20,30]
combined_dict = {k:v for k,v in zip(keys,values)}
print(combined_dict)


square = {x:x**2 for x in range(1,10) if x%2==0}
print(square)

flipped_dict = {v:k for k,v in combined_dict.items()}
print(flipped_dict)