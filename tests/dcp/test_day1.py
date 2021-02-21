import pytest

from dcp.day1 import find_match_v2


class TestDay1:
    @pytest.mark.parametrize(
        "element_sum,list_of_nums", [(25, [10, 15, 3, 7])]
    )
    def test_day1(self, element_sum, list_of_nums):
        assert (
            find_match_v2(element_sum=element_sum, list_of_nums=list_of_nums)
            is True
        )
