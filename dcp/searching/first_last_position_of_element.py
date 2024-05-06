class Solution:
    def searchRange(self, nums, target):

        lower_bound = self.findBound(nums, target, True)
        if (lower_bound == -1):
            return [-1, -1]

        upper_bound = self.findBound(nums, target, False)

        return [lower_bound, upper_bound]

    def findBound(self, nums, target, isFirst):

        N = len(nums)
        begin, end = 0, N - 1
        while begin <= end:
            mid = int((begin + end) / 2)

            if nums[mid] == target:

                if isFirst:
                    # This means we found our lower bound.
                    if mid == begin or nums[mid - 1] < target:
                        return mid

                    # Search on the left side for the bound.
                    end = mid - 1
                else:

                    # This means we found our upper bound.
                    if mid == end or nums[mid + 1] > target:
                        return mid

                    # Search on the right side for the bound.
                    begin = mid + 1

            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1

        return -1


if __name__ == "__main__":
    s = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(s.searchRange(nums, target))

    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    print(s.searchRange(nums, target))

    nums = []
    target = 0
    print(s.searchRange(nums, target))
