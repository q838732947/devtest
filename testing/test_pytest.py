
class TestCalc:
    def setup(self):
        from pythons.calc import Calc
        self.calc = Calc()

    def test_add(self):
        assert self.calc.add(1, 2) == 3

    def test_div(self):
        assert self.calc.div(2, 1) == 2

    def test_add2(self):
        assert self.calc.add2((1, 2)) == 3
