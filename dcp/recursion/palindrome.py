def is_palindrome(S, i, j):
    if i >= j:
        return True
    return S[i] == S[j] and is_palindrome(S, i + 1, j - 1)


def is_palindrome_v1(ip):
    if len(ip) == 0 or len(ip) == 1:
        return True

    if ip[0] == ip[len(ip) - 1]:
        return is_palindrome_v1(ip[1 : len(ip) - 1])

    return False


if __name__ == "__main__":
    S = "xyyzzpzzyyx"
    print(is_palindrome(S, 0, len(S) - 1))

    s = "kayak"
    print(is_palindrome_v1(s))
