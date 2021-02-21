import pytest

from ctc.check_permutation import is_permutation


class TestCheckPermutation:
    @pytest.mark.parametrize(
        "input_string, string, output",
        [("abcd", "acdb", True), ("dixit", "diitt", False)],
    )
    def test_day1(self, input_string, string, output):
        assert (
            is_permutation(input_string=input_string, string=string) == output
        )
