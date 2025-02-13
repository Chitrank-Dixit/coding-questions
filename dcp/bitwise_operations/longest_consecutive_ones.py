def longest_consecutive_ones(n: int) -> int:
    max_count = 0
    count = 0

    while n > 0:
        if n & 1:  # Check if the last bit is 1
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0  # Reset if a 0 is found
        n >>= 1  # Shift right

    return max_count

if __name__ == "__main__":
    # Example usage
    n = 222  # Binary: 11011110
    print(longest_consecutive_ones(n))  # Output: 3