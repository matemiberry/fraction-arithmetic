import unittest
from fraction_methods import Fraction


class TestStringMethods(unittest.TestCase):

    def test_division(self):
        self.assertEqual(str(Fraction.__truediv__(Fraction(1, 4), Fraction(1, 2))), '1/2')

    def test_long_division(self):
        self.assertEqual(str(Fraction.__truediv__(Fraction(1111111, 22222222), Fraction(3333333, 44444444))), '2/3')

    def test_addition(self):
        self.assertEqual(str(Fraction.__add__(Fraction(25, 100), Fraction(13, 76))), '8/19')

    def test_long_addition(self):
        self.assertEqual(str(Fraction.__add__(Fraction(13123124231231312, 232423412424131313),
                                              Fraction(123123121, 2312312))),
                         '28647040688766589907901217/537435445629267924625656')

    def test_subtraction(self):
        self.assertEqual(str(Fraction.__sub__(Fraction(25, 100), Fraction(13, 76))), '3/38')

    def test_long_subtraction(self):
        self.assertEqual(str(Fraction.__sub__(Fraction(1111111, 44444444),
                                              Fraction(4444444, 88888888))), '-1111111/44444444')

    def test_multiplication(self):
        self.assertEqual(str(Fraction.__mul__(Fraction(90, 170), Fraction(73, 265))), '657/4505')

    def test_long_multiplication(self):
        self.assertEqual(str(Fraction.__mul__(Fraction(1111111, 22222222), Fraction(73, 265))), '1111111/80669710')

    def test_zero_addition(self):
        self.assertEqual(str(Fraction.__add__(Fraction(25, 100), Fraction(0, 76))), '1/4')

    def test_zero_subtraction(self):
        self.assertEqual(str(Fraction.__sub__(Fraction(25, 100), Fraction(0, 76))), '1/4')

    def test_zero_division(self):
        self.assertEqual(str(Fraction.__truediv__(Fraction(0, 100), Fraction(1, 76))), '0')

    def test_zero_multiplication(self):
        self.assertEqual(str(Fraction.__mul__(Fraction(25, 100), Fraction(0, 76))), '0')

    def test_convert_to_periodic(self):
        self.assertEqual(str(Fraction.convert_to_periodic(Fraction(1, 3))), '0.(3)')
        self.assertEqual(str(Fraction.convert_to_periodic(Fraction(1, 666))), '0.0(015)')
        self.assertEqual(str(Fraction.convert_to_periodic(Fraction(13, 73))), '0.(17808219)')
        self.assertEqual(str(Fraction.convert_to_periodic(Fraction(0, 3))), '0')
        self.assertEqual(str(Fraction.convert_to_periodic(Fraction(12, 3))), '4')

    def test_convert_to_rational(self):
        self.assertEqual(str(Fraction.convert_to_rational('0.(3)')), '1/3')
        self.assertEqual(str(Fraction.convert_to_rational('0.0(015)')), '1/666')
        self.assertEqual(str(Fraction.convert_to_rational('0.(17808219)')), '13/73')
        self.assertEqual(str(Fraction.convert_to_rational('0')), '0')
        self.assertEqual(str(Fraction.convert_to_rational('4')), '4')


if __name__ == '__main__':
    unittest.main()
