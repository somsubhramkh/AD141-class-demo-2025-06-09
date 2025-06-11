#!/usr/bin/env python3
class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)

    def __lt__(self, other):
        left = self.numerator / self.denominator
        right = other.numerator / other.denominator
        return left < right

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
    

def main():
    fractions = [Fraction(1, 3), Fraction(), Fraction(3, 4)]
    for fraction in fractions:
        print(fraction)

    frac_1_3, frac_0_1, frac_3_4 = fractions    # unpacking
    print(frac_1_3, "<", frac_0_1, ":", frac_1_3 < frac_0_1)  # False
    print(frac_1_3, "<", frac_3_4, ":", frac_1_3 < frac_3_4)  # True
    result = frac_1_3 * frac_3_4
    print(frac_1_3, "*", frac_3_4, "=", result)  # 1/3 * 3/4 = 3/12


if __name__ == "__main__":
    main()