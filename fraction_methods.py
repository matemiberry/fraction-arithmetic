from __future__ import division
import re


class Fraction:
    den = None
    num = None

    def __init__(self, num, den):
        if den == 0:
            raise ValueError("Знаменатель не должен быть равен нулю")

        self.num = num
        self.den = den

    @staticmethod
    def gcd_euclidean(a, b):
        while b:
            a, b = b, a % b
        return a

    @classmethod
    def invert(cls, fraction):
        return cls(fraction.den, fraction.num)

    @classmethod
    def from_string(cls, text):
        return cls(*[int(i) for i in text.split('/')])

    def simplify(self):
        fact = self.gcd_euclidean(self.num,
                                  self.den)
        return Fraction(self.num // fact, self.den // fact)

    def __mul__(self, fraction):
        return Fraction.simplify(
            Fraction(self.num * fraction.num,
                     self.den * fraction.den))

    def __add__(self, fraction):
        common_den = self.gcd_euclidean(
            self.den, fraction.den)
        num1 = self.num * fraction.den
        num2 = fraction.num * self.den
        return Fraction.simplify(
            Fraction(num1 + num2, fraction.den * self.den))

    def __sub__(self, fraction):
        return self + Fraction(-fraction.num,
                               fraction.den)

    def __truediv__(self, fraction):
        return self * self.invert(fraction)

    def __repr__(self):
        if self.num == 0:
            return '{}'.format(0)
        elif self.den == 1:
            return '{}'.format(self.num)
        elif self.num != self.den:
            return '{}/{}'.format(self.num, self.den)
        elif self.num == self.den:
            return '{}'.format(1)

    def convert_to_periodic(self):
        if self.num == 0:
            return '{}'.format(0)
        elif self.num % self.den == 0:
            return '{}'.format(self.num // self.den)
        ans = str(self.num // self.den) + "."
        l_index = {}
        index = 0
        self.num = self.num % self.den
        l_index[self.num] = index
        t = False
        while not t:
            if self.num == 0:
                break
            digit = self.num * 10 // self.den
            self.num = self.num * 10 - (self.num * 10 // self.den) * self.den
            if self.num not in l_index:
                ans += str(digit)
                index += 1
                l_index[self.num] = index
                t = False
            else:
                ans += str(digit) + ")"
                ans = ans[:l_index.get(self.num) + len(
                    ans[:ans.index(".") + 1])] + "(" + ans[l_index.get(self.num) + len(ans[:ans.index(".") + 1]):]
                t = True
        return ans

    def convert_to_rational(self):
        raw = re.match(r'(\d+)[.]?(\d*)[(]?(\d*)[)]?', self).groups()
        input_raw = '{}.{}.{}'.format(raw[0], raw[1], raw[2])
        _ = lambda intnum, preper: preper and _(preper, intnum % preper) or intnum
        intnum, preper, period = input_raw.split('.')
        t = bool(period)
        num, dec = int(intnum+preper+period)-t*int(intnum+preper), (10**len(period)-t)*10**len(preper)
        fract = _(num, dec)
        if num/fract == 0:
            return '{}'.format(0)
        elif num/fract % dec/fract == 0:
            return '{}'.format(int(num/fract))
        else:
            return '{}/{}'.format(int(num/fract), int(dec/fract))
