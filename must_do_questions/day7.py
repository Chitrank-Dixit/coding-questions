import re


def palindromes(str):
    str = re.sub(r"[^a-zA-z0-9]", "", str).lower()

    i = 0
    j = len(str) - 1
    diff_count = 0
    while i < (len(str) // 2) and j >= (len(str) // 2):
        if str[i] != str[j]:
            diff_count += 1
        i += 1
        j -= 1
    return diff_count


def almost_palindrome(arr):
    diff_count = palindromes(arr)

    if diff_count in [0, 1]:
        return True
    return False


def palindromes_v1(arr, left, right):
    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1

    return True


def almost_palindrome_v1(arr):
    arr = re.sub(r"[^a-zA-z0-9]", "", arr).lower()
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] != arr[right]:
            return palindromes_v1(arr, left + 1, right) or palindromes_v1(
                arr, left, right - 1
            )
        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    a = "a"
    print(almost_palindrome(a))
    a = ""
    print(almost_palindrome(a))
    a = "abababa"
    print(almost_palindrome(a))
    a = "A man, a plan, a Canal: Panama"
    print(almost_palindrome(a))
    a = "racecar"
    print(almost_palindrome(a))
    a = "race a car"
    print(almost_palindrome(a))
    a = "abcdefdba"
    print(almost_palindrome(a))

    print("---------------------------")
    a = "a"
    print(almost_palindrome_v1(a))
    a = ""
    print(almost_palindrome_v1(a))
    a = "abababa"
    print(almost_palindrome_v1(a))
    a = "A man, a plan, a Canal: Panama"
    print(almost_palindrome_v1(a))
    a = "racecar"
    print(almost_palindrome_v1(a))
    a = "race a car"
    print(almost_palindrome_v1(a))
    a = "abcdefdba"
    print(almost_palindrome_v1(a))
