#!/usr/bin/env python3

sqr_number = lambda a: a*a
print(sqr_number(5))

# Lambdas with map

numbers_list = [1,2,3,4,5]
sqr_list = list(map(lambda a: a*a,numbers_list))
print(sqr_list)

# Lambdas with filter

even_numbers = list(filter(lambda a: a % 2 == 0,numbers_list))
print(even_numbers)


persons = [("John",30),("Steven",32),("Owen",31)]
sorted_persons_list =  sorted(persons,key=lambda person: person[1])
print(sorted_persons_list)