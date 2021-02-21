import pytest

from dcp.day2 import division_of_numbers


class TestDay1:
    @pytest.mark.parametrize(
        "arr, output",
        [([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]), ([3, 2, 1], [6, 3, 2])],
    )
    def test_day1(self, arr, output):
        assert division_of_numbers(arr=arr) == output
