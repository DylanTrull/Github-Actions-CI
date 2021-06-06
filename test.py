import unittest
import calc


class CalcultaroTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(calc.subtract(10, 5), 5)

    def test_div(self):
        self.assertEqual(calc.division(10, 2), 5)

    def test_multiply(self):
        self.assertEqual(calc.multiply(5, 2), 10)


if __name__ == '__main__':
    unittest.main()
