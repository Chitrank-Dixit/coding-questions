def prime_in_range(n):
    for i in range(2, n):
        prime_count = 0
        for j in range(2, n):
            if i % j == 0:
                prime_count += 1
        if prime_count == 1:
            print(i)


if __name__ == "__main__":
    print(prime_in_range(30))
