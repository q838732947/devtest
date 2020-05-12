import pytest

from . import is_leap_year


class TestAssert:
    @pytest.mark.p2
    def test_exception_typeerror(self):
        with pytest.raises(TypeError):
            is_leap_year.is_leap_year('ss')

    @pytest.mark.p2
    def test_exception_typeerror2(self):
        with pytest.raises(ValueError) as execinfo:
            is_leap_year.is_leap_year(0)
        assert "从公元一年开始" in str(execinfo.value)
        assert execinfo.type == ValueError

    @pytest.mark.parametrize("year", [400, 2004])
    def test_true(self, year):
        assert is_leap_year.is_leap_year(year) is True

    @pytest.mark.xfail(raises=ValueError)
    def test_a(self):
        is_leap_year.is_leap_year(-100)

    @pytest.mark.p1
    def test_exception_match(self):
        with pytest.raises(ValueError, match=r'公元元年是从公元一年开始！！') as excinfo:
            is_leap_year.is_leap_year(0)
        assert excinfo.type == ValueError
