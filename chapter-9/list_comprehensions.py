#!/usr/bin/env python3

square = [x**2 for x in range(1,10)]
print(square)

#Add a condition

square = [x**2 for x in range(1,10) if x%2==0]
print(square)

# String conversions

fruits = ["banana","apple","kiwi"]
uppercase_fruits = [fruit.upper() for fruit in fruits]
print(uppercase_fruits)

texts = ["Spam","eggS","BaCon"]
cleaned = [text.lower() for text in texts]
print(cleaned)

# nested loops

pairs = [(x,y) for x in [1,2] for y in [3,4]]
print(pairs)

# if else

labels = ["even" if x%2==0 else "odd" for x in range(1,10)]
print(labels)

values = [10,None,20,30,None,60]
filtered_values = [x for x in values if x is not None]
print(filtered_values)