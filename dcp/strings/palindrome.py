def palindrome(s):
    i = 0
    j = len(s) - 1

    while i < len(s) and j >= 0:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == "__main__":
    s = "asa"
    print(palindrome(s))

    s = "ababa"
    print(palindrome(s))

    s = "goodbook"
    print(palindrome(s))
