class Rational:
    def __init__(self, a=1, b=1):
        if b == 0:
            raise ValueError("Denominator cannot be zero.")
        self.a = a
        self.b = b

    # Simplify the rational number
    def simplify(self):
        from math import gcd
        common = gcd(self.a, self.b)
        self.a //= common
        self.b //= common

    # String representation
    def __str__(self):
        return f"{self.a} / {self.b}"

    # Binary operators
    def __add__(self, other):
        s = Rational()
        s.a = self.a * other.b + self.b * other.a
        s.b = self.b * other.b
        s.simplify()
        return s

    def __sub__(self, other):
        s = Rational()
        s.a = self.a * other.b - self.b * other.a
        s.b = self.b * other.b
        s.simplify()
        return s

    def __mul__(self, other):
        s = Rational()
        s.a = self.a * other.a
        s.b = self.b * other.b
        s.simplify()
        return s

    def __truediv__(self, other):
        if other.a == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        s = Rational()
        s.a = self.a * other.b
        s.b = self.b * other.a
        s.simplify()
        return s

    # Comparison operators
    def __eq__(self, other):
        return self.a * other.b == self.b * other.a

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.a * other.b < self.b * other.a

    def __le__(self, other):
        return self.a * other.b <= self.b * other.a

    def __gt__(self, other):
        return self.a * other.b > self.b * other.a

    def __ge__(self, other):
        return self.a * other.b >= self.b * other.a

    # Assignment operators
    def __iadd__(self, other):
        self.a = self.a * other.b + self.b * other.a
        self.b = self.b * other.b
        self.simplify()
        return self

    def __isub__(self, other):
        self.a = self.a * other.b - self.b * other.a
        self.b = self.b * other.b
        self.simplify()
        return self

    def __imul__(self, other):
        self.a *= other.a
        self.b *= other.b
        self.simplify()
        return self

    def __itruediv__(self, other):
        if other.a == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        self.a *= other.b
        self.b *= other.a
        self.simplify()
        return self

r1 = Rational(2, 3)
r2 = Rational(2, 5)

# Binary operators
print("Addition:", r1 + r2)        # Output: 16 / 15
print("Subtraction:", r1 - r2)    # Output: 4 / 15
print("Multiplication:", r1 * r2) # Output: 4 / 15
print("Division:", r1 / r2)       # Output: 10 / 6 (simplified to 5 / 3)

# Comparison operators
print("Equal:", r1 == r2)         # Output: False
print("Not Equal:", r1 != r2)     # Output: True
print("Less than:", r1 < r2)      # Output: False
print("Less than or equal:", r1 <= r2) # Output: False
print("Greater than:", r1 > r2)   # Output: True
print("Greater than or equal:", r1 >= r2) # Output: True

# Assignment operators
r1 += r2
print("After += :", r1)           # Output: 16 / 15
r1 -= r2
print("After -= :", r1)           # Output: 2 / 3
r1 *= r2
print("After *= :", r1)           # Output: 4 / 15
r1 /= r2
print("After /= :", r1)           # Output: 10 / 6 (simplified to 5 / 3)
