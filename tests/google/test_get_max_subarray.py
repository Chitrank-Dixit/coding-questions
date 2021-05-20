import pytest

from google.get_max_subarray import get_max_subarray


class TestDay1:
    @pytest.mark.parametrize(
        "array,k,output", [([10, 5, 2, 7, 8, 7], 3, [10, 7, 8, 8])]
    )
    def test_day1(self, array, k, output):
        assert get_max_subarray(array=array, k=k) == output
