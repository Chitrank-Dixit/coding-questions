class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            end_val = nums.pop()
            nums.insert(0, end_val)
        return nums


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    s = Solution()
    print(s.rotate(nums=arr, k=3))
