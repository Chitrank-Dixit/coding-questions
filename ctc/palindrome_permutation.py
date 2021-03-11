from dcp.permutations import permutation


def palindrome_permutation(str):
    data = list(str.lower())
    palindromes = set()
    for p in permutation(data):
        is_palindrome = True
        current_permutation = "".join([e for e in p if e != " "])
        i = 0
        j = len(current_permutation) - 1

        while i <= len(current_permutation) - 1 and j >= 0:
            if current_permutation[i] != current_permutation[j]:
                is_palindrome = False
                break
            i += 1
            j -= 1

        if is_palindrome:
            palindromes.add("".join(p))
    return palindromes


if __name__ == "__main__":
    ip = "Tact Coa"

    print(palindrome_permutation(ip))
