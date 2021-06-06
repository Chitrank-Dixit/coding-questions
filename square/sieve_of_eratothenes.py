"""
The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. The method is to take
increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), then
[6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N, the unmarked
numbers that remain will be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).
"""


def SieveOfEratosthenes(n):
    # Create a boolean array
    # "prime[0..n]" and initialize
    #  all entries it as true.
    # A value in prime[i] will
    # finally be false if i is
    # Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:

        # If prime[p] is not
        # changed, then it is a prime
        if prime[p] is True:

            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, n + 1):
        if prime[p]:
            print(p)


# Driver code
if __name__ == "__main__":
    n = 30
    print(
        "Following are the prime numbers smaller",
    )
    print("than or equal to", n)
    SieveOfEratosthenes(n)
