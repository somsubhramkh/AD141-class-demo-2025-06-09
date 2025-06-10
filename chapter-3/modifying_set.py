#!/usr/bin/env python3

numbers = {10,20,30}
numbers.add(40)
print(numbers)
numbers.add(50)
print(numbers)

# no duplicate items will be allowed
numbers.add(50)
print(numbers)

numbers.update([60,70,70,90])
print(numbers)

# removal of items

numbers.remove(90)
print(numbers)

# throws exception when element is not found
# numbers.remove(35)
# print(numbers)

# will not throw exception when element is not found
numbers.discard(35)
print(numbers)

print(numbers.pop(),numbers)