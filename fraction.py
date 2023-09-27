# gcd function
def gcd(m, n):
    if max(m,n) % min(m,n) == 0:
        return min(m, n)
    else:
        return gcd(n, m % n)
# Fraction class
# Implements: addition and equality
# To do: multiplication, division, subtraction and comparison operators (< , >)
class Fraction:
    def __init__(self, top, bottom):
        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common
        if type(top) != int or type(bottom) != int:
            raise Exception('Numerator or denominator is not an integer.')
        if self.den < 0:
            self.num = -1*self.num
            self.den = -1*self.den

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, other):
        if type(other) == int:
            k = 1
            l = other
        else:
            k = other.den
            l = other.num

        new_num = self.num * k + self.den * l
        new_den = self.den * k

        return Fraction(new_num, new_den)

    def __radd__(self, other):
        new_num = self.num + self.den*other
        new_den = self.den

        return Fraction(new_num, new_den)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num == second_num

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)

        return Fraction(new_num // common, new_den // common)

    def __sub__(self, other):
        new_num = self.num * other.den - self.den*other.num
        new_den = self.den * other.den

        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        common = gcd(new_num, new_den)

        return Fraction(new_num // common, new_den // common)

    def __lt__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num < second_num

    def __gt__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num > second_num

    def __ge__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num >= second_num

    def __le__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num <= second_num

    def __ne__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num != second_num

    def __iadd__(self, other):
        if type(other) == int:
            k = 1
            l = other
        else:
            k = other.den
            l = other.num

        self.num = self.num * k + self.den * l
        self.den = self.den * k

        return Fraction(self.num, self.den)

    def __repr__(self):
        return f'Fraction({self.num},{self.den})'




x = Fraction(1, -2)
y = Fraction(2, 3)
print(x+3)
print(x < y)
print()


