import unittest


class TestCalc(unittest.TestCase):
    def setUp(self) -> None:
        from pythons.calc import Calc
        self.calc = Calc()

    def test_add_1(self):
        self.assertEqual(3, self.calc.add(1, 2))

    def test_add_2(self):
        self.assertEqual(0.03, self.calc.add(0.01, 0.02))


if __name__ == '__main__':
    unittest
