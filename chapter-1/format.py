#!/usr/bin/env python3

separator = "----------------------------"
name_format = "First: {} \t Last: {}  \tMiddle Initial: {} "
print(name_format.format("John","Doe","A"))
print(name_format.format("Melany","Jones","C"))

dimensions = "Type: {type}\nHeight:{height}, Width:{width}"
print(dimensions.format(height=50,width=20,type="Package"))

name = "{1} {0}"

print(name.format("John","Doe"))