"""

Optimized solution explaination

Why is it better?
	•	Exponentiation by squaring reduces the time complexity to O(\log n), where n is the absolute value of the exponent. This is much faster than the O(n) approach in the previous version.
	•	Handles all cases (positive, negative, and zero exponents) efficiently.

exponentiation by squaring in more detail.

What is Exponentiation by Squaring?

This technique reduces the number of multiplications needed to compute ￼. Instead of multiplying the base repeatedly, it leverages the mathematical property:

￼

By squaring the base and halving the exponent at each step, we significantly reduce the number of multiplications.

Key Steps in the Code
	1.	Handle Special Cases:
	•	If ￼, the result is always 1.
	•	If ￼, compute the reciprocal of the base and make the exponent positive (e.g., ￼).
	2.	Iterative Squaring:
	•	Use a loop to calculate ￼.
	•	If the exponent is odd, multiply the result by the current base.
	•	Square the base and halve the exponent for the next iteration.
	•	Repeat until the exponent becomes 0.
	3.	Optimization Benefits:
	•	Instead of performing ￼ multiplications (for ￼), this method reduces it to ￼, because the exponent is halved at each step.
	•	For example:
	•	￼: Instead of ￼ (10 multiplications), it calculates:
	•	￼, ￼, ￼, and then multiplies as needed, reducing the steps to just 4!

Walkthrough Example

Let’s compute ￼ step by step:
	1.	Start with:
	•	base = 2, exponent = 10, result = 1.
	2.	First Iteration:
	•	exponent is even, so:
	•	Square the base: ￼.
	•	Halve the exponent: ￼.
	3.	Second Iteration:
	•	exponent is odd, so:
	•	Multiply result by base: ￼.
	•	Square the base: ￼.
	•	Halve the exponent: ￼.
	4.	Third Iteration:
	•	exponent is even, so:
	•	Square the base: ￼.
	•	Halve the exponent: ￼.
	5.	Fourth Iteration:
	•	exponent is odd, so:
	•	Multiply result by base: ￼.
	•	Square the base (not needed here as exponent becomes 0).
	6.	Final Step:
	•	exponent is now 0, so the loop ends. The final result is 1024.

Benefits Recap:
	•	Speed: Reduces multiplications from 10 to just 4 for ￼. As the exponent grows, the time savings increase exponentially.
	•	Efficiency: This method uses fewer resources and works well for large numbers or high exponents.


"""

def power_v1(base, exponent):
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    if exponent < 0:
        return 1 / result
    return result


def power_v2(base, exponent):
    if exponent == 0:
        return 1
    if exponent < 0:
        base = 1 / base
        exponent = -exponent

    result = 1
    while exponent > 0:
        if exponent % 2 == 1:  # If the exponent is odd
            result *= base
        base *= base  # Square the base
        exponent //= 2  # Halve the exponent (integer division)

    return result


if __name__ == "__main__":
    print(power_v1(2, 3))   # Output: 8
    print(power_v1(5, -2))  # Output: 0.04
    print(power_v1(3, 0))   # Output: 1

    # Example usage:
    print(power_v2(2, 10))  # Output: 1024
    print(power_v2(5, -3))  # Output: 0.008
    print(power_v2(3, 0))  # Output: 1