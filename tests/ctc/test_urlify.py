import pytest

from ctc.urlify import urlify


class TestUrlify:
    @pytest.mark.parametrize(
        "string, output", [("   Mr Chitrank Dixit  ", "Mr%20Chitrank%20Dixit")]
    )
    def test_day1(self, string, output):
        assert urlify(string=string) == output
