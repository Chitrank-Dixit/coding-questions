"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""


# !/bin/python3


class Solution:
    @staticmethod
    def set_counters():
        i = 1
        prev_index = 0
        return i, prev_index

    def remove_duplicates(self, nums):
        i, prev_index = self.set_counters()
        while i < len(nums):
            if nums[i] == nums[prev_index]:
                if (i < len(nums)) and (i > 0):
                    nums.pop(i)
                if i - 1 != 0:
                    i -= 1
                    prev_index = i - 1
                else:
                    i, prev_index = self.set_counters()
            else:
                i += 1
                prev_index += 1
        return nums


if __name__ == "__main__":
    s = Solution()
    print(s.remove_duplicates([1, 1, 1]))
    print(s.remove_duplicates([1, 1, 1, 1]))
    print(s.remove_duplicates([1, 1, 2]))
    print(s.remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(s.remove_duplicates([-1, 0, 0, 0, 0, 3, 3]))
