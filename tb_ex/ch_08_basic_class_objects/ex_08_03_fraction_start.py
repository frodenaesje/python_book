# file: ex_08_03_fraction_start.py

class Fraction:

    @staticmethod
    def gcd(a, b):
        # Euclid's algorithm - do not modify
        while b:
            a, b = b, a % b
        return a

    def __init__(self, numerator, denominator):
        # TODO: raise ValueError if denominator is zero
        # TODO: reduce the fraction by dividing both by gcd
        #       Hint: g = Fraction.gcd(abs(numerator), abs(denominator))
        #             self._numerator = numerator // g
        #             self._denominator = denominator // g
        pass

    def __str__(self):
        # TODO: return "numerator/denominator" or just "numerator" if denominator == 1
        pass

    def __add__(self, other):
        # TODO: a/b + c/d = (a*d + c*b) / (b*d)
        # Return a new Fraction (it will be reduced automatically)
        pass

    def __mul__(self, other):
        # TODO: a/b * c/d = (a*c) / (b*d)
        pass

    def __eq__(self, other):
        # TODO: a/b == c/d when a*d == b*c
        pass

    def __lt__(self, other):
        # TODO: compare by value: a/b < c/d when a*d < b*c
        pass


if __name__ == "__main__":
    f1 = Fraction(3, 4)
    f2 = Fraction(6, 8)
    f3 = Fraction(4, 1)

    print(f"Fraction(3, 4): {f1}")
    print(f"Fraction(6, 8): {f2}   (reduced automatically)")
    print(f"Fraction(4, 1): {f3}")

    print(f"\n1/2 + 1/3  = {Fraction(1,2) + Fraction(1,3)}")
    print(f"1/2 * 2/3  = {Fraction(1,2) * Fraction(2,3)}")
    print(f"3/4 == 6/8 = {Fraction(3,4) == Fraction(6,8)}")
    print(f"1/2 < 3/4  = {Fraction(1,2) < Fraction(3,4)}")

    fracs = [Fraction(1,2), Fraction(3,4), Fraction(1,3), Fraction(2,3), Fraction(1,4)]
    print(f"\nsorted: {sorted(fracs)}")
