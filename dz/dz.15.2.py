from math import gcd

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Знаменник не може бути нулем!")
        self.a = a
        self.b = b

    def simplify(self):
        common_divisor = gcd(self.a, self.b)
        self.a //= common_divisor
        self.b //= common_divisor

    def __add__(self, other):
        if isinstance(other, Fraction):
            numerator = self.a * other.b + other.a * self.b
            denominator = self.b * other.b
            return Fraction(numerator, denominator)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Fraction):
            numerator = self.a * other.b - other.a * self.b
            denominator = self.b * other.b
            return Fraction(numerator, denominator)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Fraction):
            numerator = self.a * other.a
            denominator = self.b * other.b
            return Fraction(numerator, denominator)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b == other.a * self.b
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b > other.a * self.b
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b < other.a * self.b
        return NotImplemented

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18', str(f_c)

f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18', str(f_d)

f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18', str(f_e)

assert f_d < f_c  
assert f_d > f_e  
assert f_a != f_b  

f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  

print("Усі тести пройдені успішно!")
