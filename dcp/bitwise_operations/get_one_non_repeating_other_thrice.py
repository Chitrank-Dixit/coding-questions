def singleNumber(nums):
    ans = 0

    for i in range(32):
        bit_sum = 0
        for num in nums:
            # Convert the number to two's complement representation to handle large test case
            if num < 0:
                num = num & (2**32-1)
            bit_sum += (num >> i) & 1
        bit_sum %= 3
        ans |= bit_sum << i

    # Convert the result back to two's complement representation if it's negative to handle large test case
    if ans >= 2**31:
        ans -= 2**32

    return ans

if __name__ == '__main__':
    nums = [2, 2, 3, 2, 5, 7, 4, 5, 6, 7, 6, 5, 7, 4, 6, 4]
    print(singleNumber(nums))