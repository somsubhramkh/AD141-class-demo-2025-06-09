#!/usr/bin/env python3

def display_profile_info(user):
    for key, value in user.items():
        print(key,value)


user_information = {
    "name": "John",
    "age": 20,
    "city": "New York"
}

display_profile_info(user_information)