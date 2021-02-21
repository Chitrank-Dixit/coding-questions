#!/bin/python3


class Solution:
    def removeDuplicates(self, nums):
        i = 1
        prev_index = 0
        while i < len(nums):
            if nums[i] == nums[prev_index]:
                if i < len(nums) and i > 0:
                    nums.pop(i)
                if i - 1 != 0:
                    i -= 1
                    prev_index = i - 1
                else:
                    i = 1
                    prev_index = 0
            else:
                i += 1
                prev_index += 1
        return len(nums)


if __name__ == "__main__":
    s = Solution()
    s.removeDuplicates([1, 1, 1])
    s.removeDuplicates([1, 1, 1, 1])
    s.removeDuplicates([1, 1, 2])
    s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    print("see output")
    s.removeDuplicates([-1, 0, 0, 0, 0, 3, 3])
