#!/usr/bin/env python3


class Student:

    def __init__(self,name,major):
        self._name = name
        self._major = major

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        self._name = name
    
    @property
    def major(self):
        return self._major
    
    @major.setter
    def major(self,major):
        self._major = major


def main():
    jeff = Student("Jeff","American History")
    heather = Student("Heather","mathematics")
    print(jeff.name,jeff.major)
    print(heather.name,heather.major)
    jeff.name = "Jeffrey"
    heather.major = "Computer Science"
    print(jeff.name,jeff.major)
    print(heather.name,heather.major)


if __name__ == "__main__":
    main()