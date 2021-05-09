import pytest

from dcp.linked_list_algos.reorder_or_fold_linked_list import (
    reorder,
    LinkedList,
)


class TestDay1:
    @pytest.mark.parametrize(
        "array,output",
        [
            ([6, 5, 4, 3, 2, 1], [1, 6, 2, 5, 3, 4]),
            ([5, 4, 3, 2, 1], [1, 5, 2, 4, 3]),
        ],
    )
    def test_day1(self, array, output):
        next_element = None
        ll = None
        for element in array:
            ll = LinkedList(element, next_element)
            next_element = ll

        head = reorder(ll)
        output_list = []
        while head:
            output_list.append(head.data)
            head = head.next_val
        assert output_list == output
