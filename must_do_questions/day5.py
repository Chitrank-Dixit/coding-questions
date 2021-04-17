"""
Given a string find the length of the longest substring without repeating characters
"""


def longest_substring_length(string):
    if len(string) <= 1:
        return len(string)

    longest = 0
    for left in range(len(string)):
        seen_chars = {}
        current_length = 0
        for right in range(left, len(string)):
            current_char = string[right]
            if current_char not in seen_chars:
                current_length += 1
                seen_chars[current_char] = True
                longest = max(longest, current_length)
            else:
                break
    return longest


def longest_substring_length_v1(string):
    """
    Sliding window technique
    """
    if len(string) <= 1:
        return len(string)
    max_length = 0
    left = 0
    seen_chars = {string[left]: left}
    for right in range(1, len(string)):
        if string[right] not in seen_chars:
            seen_chars[string[right]] = right
        else:
            length = right - left
            if max_length < length:
                max_length = length
            seen_chars = {string[right]: right}
            left = right
    return max_length


def longest_substring_length_v2(string):
    """
    Sliding window technique
    """
    if len(string) <= 1:
        return len(string)
    max_length = 0
    left = 0
    seen_chars = {}
    for right in range(0, len(string)):
        current_char = string[right]
        if current_char in seen_chars:
            prev_seen_char = seen_chars[current_char]

            if prev_seen_char >= left:
                left = prev_seen_char + 1

        seen_chars[current_char] = right
        max_length = max(max_length, (right - left) + 1)
    return max_length


if __name__ == "__main__":
    string = "abccabb"
    print(longest_substring_length(string=string))

    string = "abccabb"
    print(longest_substring_length_v1(string=string))

    string = "abccabb"
    print(longest_substring_length_v2(string=string))
