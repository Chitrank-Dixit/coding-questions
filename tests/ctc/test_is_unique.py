import pytest

from ctc.is_unique import is_uniqe


class TestIsUnique:
    @pytest.mark.parametrize(
        "string, output", [("chitrank", True), ("dixit", False)]
    )
    def test_day1(self, string, output):
        assert is_uniqe(string) == output
