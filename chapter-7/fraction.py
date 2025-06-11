#!/usr/bin/env python3
class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, denominator):
        if denominator == 0:
            raise ZeroDivisionError()
        self._denominator = denominator

    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)
    

def main():
    try:
        while True:
            numer = int(input("Please enter a numerator"))
            denom = int(input("Please enter a denominator"))
            fraction = Fraction(numer, denom)
            print(fraction)
    except ZeroDivisionError:
        print("Zero Division Error")


if __name__ == "__main__":
    main()