#!/usr/bin/env python3

data = "\t  \nabc  def\t  \n"
# print(data)
result = data.strip()
print(len(data))
print(len(result))
print(len(data.lstrip()))
print(len(data.rstrip()))