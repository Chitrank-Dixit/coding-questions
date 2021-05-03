import re


def palindromes(str):
    str = re.sub(r"[^a-zA-z0-9]", "", str).lower()

    i = 0
    j = len(str) - 1

    while i < (len(str) // 2) and j >= (len(str) // 2):
        if str[i] != str[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == "__main__":
    a = "a"
    print(palindromes(a))
    a = ""
    print(palindromes(a))

    a = "abababa"
    print(palindromes(a))

    a = "A man, a plan, a Canal: Panama"
    print(palindromes(a))

    a = "racecar"
    print(palindromes(a))

    a = "race a car"
    print(palindromes(a))
