#!/usr/bin/env python3

class AgeTooSmallError(Exception):
    def __init__(self, message="Age is below the allowed limit"):
        self._message = message
        super().__init__(self._message)



def check_age(age):
    if age < 18:
        raise AgeTooSmallError("You must be at least 18 years old")
    else:
        print(age)


def main():
    try:
        user_age = int(input("Enter age"))
        check_age(user_age)
    except AgeTooSmallError as err:
        print(err)
    except ValueError:
        print("Please enter number only")


main()