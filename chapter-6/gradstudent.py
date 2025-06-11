#!/usr/bin/env python3
from student3 import Student


class GradStudent(Student):
    def __init__(self, name, major, stipend):
        super().__init__(name, major)
        self.stipend = stipend

    @property
    def stipend(self):
        return self._stipend

    @stipend.setter
    def stipend(self, stipend):
        self._stipend = stipend

    def __str__(self):
        # Override the __str__ from the parent class by
        # first getting the parent information:
        # super().__str__()
        # and then concatenating the stipend
        return "{} {}".format(super().__str__(), self.stipend)
    

def main():
    grad_student = GradStudent("James", "Anthropology", 25000)

    print("  MAJOR:", grad_student.major)
    print("   NAME:", grad_student.name)
    print("STIPEND:", grad_student.stipend)
    print(grad_student)


if __name__ == "__main__":
    main()