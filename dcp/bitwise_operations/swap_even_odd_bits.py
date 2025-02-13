def swap_odd_even_bits(n: int) -> int:
    EVEN_MASK = 0xAAAAAAAA  # 10101010 10101010 10101010 10101010 (select even bits)
    ODD_MASK  = 0x55555555  # 01010101 01010101 01010101 01010101 (select odd bits)

    even_bits = (n & EVEN_MASK) >> 1  # Move even bits to odd positions
    odd_bits  = (n & ODD_MASK) << 1   # Move odd bits to even positions

    return even_bits | odd_bits  # Combine both


if __name__ == "__main__":
    # Example usage
    n = 23  # Binary: 00010111
    result = swap_odd_even_bits(n)
    print(result)  # Output: 43
    print(bin(result))  # Output: 0b101011