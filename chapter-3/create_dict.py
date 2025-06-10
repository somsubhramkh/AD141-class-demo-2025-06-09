#!/usr/bin/env python3

empty_dict = {}
print(empty_dict,type(empty_dict))


student = {"name": "John", "age": 20, 
           "major": "Computer Science"}

print(student)

# # access elements from dict

# print(student["name"], student["age"])

# # using get() 
# print(student.get('name'))
# print(student.get('gpa','Not available'))


student["age"] = 21
print(student)

# adding a key-value pair
student["city"] = "Boston"
print(student)

# remove key-value pair
print(student.pop("age"))
print(student)

# # iterating through key

# for key in student:
#     print(key)


# # iterating through value

# for key in student.values():
#     print(key)

# iterating through items

for key,value in student.items():
    print(key,value)