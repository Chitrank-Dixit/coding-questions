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


if __name__ == "__main__":
    string = "abccabb"
    print(longest_substring_length(string=string))
