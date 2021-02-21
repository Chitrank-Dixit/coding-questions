import pytest

from leetcode.remove_duplicates import Solution


class TestDay1:
    @pytest.mark.parametrize(
        "array,output",
        [
            ([1, 1, 1], [1]),
            ([1, 1, 1, 1], [1]),
            ([1, 1, 2], [1, 2]),
            ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),
            ([-1, 0, 0, 0, 0, 3, 3], [-1, 0, 3]),
        ],
    )
    def test_day1(self, array, output):
        s = Solution()
        assert s.remove_duplicates(array) == output
