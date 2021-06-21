def factorial(n, total_so_far=1):
    if n == 0:
        return total_so_far
    return factorial(n - 1, total_so_far * n)


if __name__ == "__main__":
    print(factorial(5))
