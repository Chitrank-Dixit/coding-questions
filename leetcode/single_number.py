class Solution:
    def singleNumber(self, nums):
        nums = sorted(nums)
        i = 1
        prev = 0
        while i < len(nums):
            if prev is None:
                prev = i
            elif nums[prev] == nums[i]:
                prev = None
            i += 1
        return nums[prev]


if __name__ == "__main__":
    s = Solution()
    nums = [2, 2, 1]
    print(s.singleNumber(nums=nums))

    nums = [4, 1, 2, 1, 2]
    print(s.singleNumber(nums=nums))
