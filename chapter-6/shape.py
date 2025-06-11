#!/usr/bin/env python3
import math

class Shape:
    id = 100

    def __init__(self, name):
        self.name = name
        self.number = Shape.id
        Shape.id += 1

    def area(self):
        pass  # Intended to be implemented by subclasses

    @property
    def name(self): return self._name

    @name.setter
    def name(self, name): self._name = name

    def __str__(self):
        return "Name:{}  id:{}".format(self.name, self.number)
    

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def __str__(self):
        fmt = "{}  Radius:{}"
        return fmt.format(super().__str__(), self.radius)

    def area(self):
        return math.pi * self.radius ** 2
    

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def __str__(self):
        fmt = "{}  Length:{} Width:{}"
        return fmt.format(super().__str__(), self.length,
                          self.width)

    def area(self):
        return self.length * self.width
    

class Square(Rectangle):
    def __init__(self, name, length):
        super().__init__(name, length, length)


def main():
    shapes = [Circle("Circle 1", 10),
              Square("Square 1", 5),
              Rectangle("Rectang1e 1", 5, 10)]

    for shape in shapes:
        print(shape)
        print("AREA:", shape.area())
        print("*" * 50)


if __name__ == "__main__":
    main()