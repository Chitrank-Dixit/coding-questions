import pytest

from dcp.mathematics.sum_of_digits import sum_of_digits


class TestDay1:
    @pytest.mark.parametrize("array,output", [(1052787, 30)])
    def test_day1(self, array, output):
        assert sum_of_digits(n=array) == output
