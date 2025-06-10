#!/usr/bin/env python3

a = {1,2,3,4,5}
b = {4,5,7,8,9}

# union

# result = a.union(b)
# print(result)

# result = a | b
# print(result)

# intersection

# result = a.intersection(b)
# print(result)

# result = a & b
# print(result)

# Difference

# result = a.difference(b)
# print(result)
# result = b.difference(a)
# print(result)

# result = a - b
# print(result)

# result = b - a
# print(result)

# Symmetric Difference

# result = a.symmetric_difference(b)
# print(result)

# result = a ^ b
# print(result)


x = {1,2}
y = {1,2,3,4,5}

print(x.issubset(y))
print(y.issubset(x))

print(x.issuperset(y))
print(y.issuperset(x))