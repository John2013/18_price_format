import unittest
from format_price import format_price


class PriceFormatTestCase(unittest.TestCase):
    def test_big_int_value(self):
        self.assertEqual(format_price(1234567890), '1 234 567 890')

    def test_float_value(self):
        self.assertEqual(format_price(123456.77), '123 456.77')

    def test_float_with_trailing_zeros(self):
        self.assertEqual(format_price(1234.00), '1 234')

    def test_float_string(self):
        self.assertEqual(format_price('12345.67'), '12 345.67')

    def test_incorrect_string(self):
        with self.assertRaises(ValueError):
            format_price('1234re')

    def test_incorrect_list(self):
        with self.assertRaises(ValueError):
            format_price(['1234'])


if __name__ == '__main__':
    unittest.main()