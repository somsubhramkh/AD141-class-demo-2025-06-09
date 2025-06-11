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

    def __str__(self):
        return "{} : {}".format(self.name,self.major)
    
    def __eq__(self, obj):
        if(type(obj)) != Student:
            return False
        else:
            return self.name == obj.name and self.major == obj.major


def main():
    s1 = Student("Elizabeth", "Electrical Engineering")
    s2 = Student("Robert", "Electrical Engineering")
    student_info("Before", s1, s2)
    s2.name = "Elizabeth"
    student_info("After", s1, s2)

def student_info(label, student1, student2):
    print(label)
    print(student1, "id=", id(student1))
    print(student2, "id=", id(student2))
    
    print(student1 == student2)
    print()


if __name__ == "__main__":
    main()