import unittest


def add_integer(a, b=98):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)

    return a + b


class AddIntegerTestCase(unittest.TestCase):
    def test_regular_addition(self):
        self.assertEqual(add_integer(2, 3), 5)

    def test_positive_with_negative(self):
        self.assertEqual(add_integer(2, -4), -2)

    def test_negative_with_positive(self):
        self.assertEqual(add_integer(-6, 8), 2)

    def test_addition_over_multiple_values(self):
        expected = [0, 2, 6, 12, 20, 30]
        result = [add_integer(i, i ** 2) for i in range(6)]
        self.assertEqual(result, expected)

    def test_float_with_int(self):
        self.assertEqual(add_integer(2.1, 4), 6)

    def test_int_with_float(self):
        self.assertEqual(add_integer(5, 7.8), 12)

    def test_both_float(self):
        self.assertEqual(add_integer(2.45, 3.1), 5)

    def test_passed_nan(self):
        with self.assertRaises(ValueError):
            add_integer(1, float('nan'))

    def test_passed_inf(self):
        with self.assertRaises(OverflowError):
            add_integer(1, float('inf'))

    def test_super_long_int(self):
        self.assertEqual(add_integer(999999999999999999999999999999, 1), 1000000000000000000000000000000)

    def test_non_number_with_number(self):
        with self.assertRaises(TypeError):
            add_integer([1], 2)

    def test_number_with_non_number(self):
        with self.assertRaises(TypeError):
            add_integer(3, "2")

    def test_non_number_with_non_number(self):
        with self.assertRaises(TypeError):
            add_integer((2,), {"key": "value"})

    def test_bool_with_number(self):
        with self.assertRaises(TypeError):
            add_integer(True, 1)

    def test_number_with_bool(self):
        with self.assertRaises(TypeError):
            add_integer(0, False)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            add_integer()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            add_integer(1)

    def test_more_than_2_args(self):
        with self.assertRaises(TypeError):
            add_integer(1, 2, 3)


if __name__ == '__main__':
    unittest.main()

