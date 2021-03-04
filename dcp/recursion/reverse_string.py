def reverse_str(s):
    if len(s) == 0:
        return []
    # print(s[len(s) - 1], s[:len(s) - 1])
    return [s[len(s) - 1]] + reverse_str(s[: len(s) - 1])


if __name__ == "__main__":
    print(reverse_str(["H", "E", "L", "L", "O"]))
