#!/usr/bin/env python3

number = int(input("Enter a number"))


if number > 90:
    print("number is greater than 90")
elif number > 75 and number <=90:
     print("number is between 76-90") 
elif number > 60 and number <=75:
     print("number is between 61-75")
else:
    print("number is less than or equal to 50")


print("This line is out of the if block")    # outside if-else block