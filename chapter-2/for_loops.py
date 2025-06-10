#!/usr/bin/env python3

word = "Hello"
print(word)

for each_char in "Hello":
    print(each_char,end="\t")


delim = "\n\t"

print("\nrange(5):",end=delim)
for i in (1,5,2):
    print(i,end=" ")