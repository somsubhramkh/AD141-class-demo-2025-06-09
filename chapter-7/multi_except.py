#!/usr/bin/env python3

def main():
    names = ['Mike', 'John',  'Jane',  'Alice']
    themap = {'Mike': 15, 'Chris': 10, 'Dave': 25}

    while True:
        try:
            value = input("Enter an Integer: ")
            if value == "end":
                break
            value = int(value)
            name = input("Enter name:")
            print("Name:",themap[name])
        except ValueError:
            print("Not a number")
        except (KeyError, IndexError) as err :
            print("value not found",err)
        except Exception as e:
            print("Unknown Exception",e)
        


if __name__ == "__main__":
    main()