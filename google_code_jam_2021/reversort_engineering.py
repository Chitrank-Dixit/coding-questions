"""
Problem
Note: The main parts of the statements of the problems "Reversort" and "Reversort Engineering" are identical, except for the last paragraph. The problems can otherwise be solved independently.

Reversort is an algorithm to sort a list of distinct integers in increasing order. The algorithm is based on the "Reverse" operation. Each application of this operation reverses the order of some contiguous part of the list.

The pseudocode of the algorithm is the following:

Reversort(L):
  for i := 1 to length(L) - 1
    j := position with the minimum value in L between i and length(L), inclusive
    Reverse(L[i..j])
After i−1 iterations, the positions 1,2,…,i−1 of the list contain the i−1 smallest elements of L, in increasing order. During the i-th iteration, the process reverses the sublist going from the i-th position to the current position of the i-th minimum element. That makes the i-th minimum element end up in the i-th position.

For example, for a list with 4 elements, the algorithm would perform 3 iterations. Here is how it would process L=[4,2,1,3]:

i=1, j=3⟶L=[1,2,4,3]
i=2, j=2⟶L=[1,2,4,3]
i=3, j=4⟶L=[1,2,3,4]
The most expensive part of executing the algorithm on our architecture is the Reverse operation. Therefore, our measure for the cost of each iteration is simply the length of the sublist passed to Reverse, that is, the value j−i+1. The cost of the whole algorithm is the sum of the costs of each iteration.

In the example above, the iterations cost 3, 1, and 2, in that order, for a total of 6.

You are given a size N and a cost C. Find a list of N distinct integers between 1 and N such that the cost of applying Reversort to it is exactly C, or say that there is no such list.

Input
The first line of the input gives the number of test cases, T. T lines follow. Each line describes a test case with two integers N and C, the size of the wanted list and the desired cost, respectively.

Output
For each test case, if there is no list of size N such that applying Reversort to it costs exactly C, output one line containing Case #x: IMPOSSIBLE, where x is the test case number (starting from 1). Otherwise, output one line containing Case #x: y1 y2 ... yN, where x is the test case number (starting from 1) and each yi is a distinct integer between 1 and N, representing the i-th element of one such possible list.

If there are multiple solutions, you may output any one of them. (See "What if a test case has multiple correct solutions?" in the Competing section of the FAQ.) This information about multiple solutions will not be explicitly stated in the remainder of the 2021 contest.

Limits
Time limit: 10 seconds.
Memory limit: 1 GB.
1≤T≤100.
1≤C≤1000.
Test Set 1 (Visible Verdict)
2≤N≤7.
Test Set 2 (Visible Verdict)
2≤N≤100.
Sample
Sample Input
save_alt
content_copy
5
4 6
2 1
7 12
7 2
2 1000
Sample Output
save_alt
content_copy
Case #1: 4 2 1 3
Case #2: 1 2
Case #3: 7 6 5 4 3 2 1
Case #4: IMPOSSIBLE
Case #5: IMPOSSIBLE
Sample Case #1 is described in the statement above.

In Sample Case #2, the algorithm runs for only one iteration on the proposed output. In that iteration, reverse is applied to a sublist of size 1, therefore, its cost is 1.

In Sample Case #3, the first iteration reverses the full list, for a cost of 7. After that, the list is already sorted, but there are 5 more iterations, each of which contributes a cost of 1. Another valid output would be 7 5 4 3 2 1 6. For that output, the first iteration has a cost of 6, the last one has a cost of 2, and all others have a cost of 1.

In Sample Case #4, Reversort will necessarily perform 6 iterations, each of which will have a cost of at least 1, so there is no way the total cost can be as low as required.
"""

from itertools import permutations


def reversort(ip_list, cost):
    total_cost = 0
    for i in range(len(ip_list) - 1):
        min_val = ip_list[i]
        j = i
        for k in range(i, len(ip_list)):
            if ip_list[k] < min_val:
                min_val = ip_list[k]
                j = k

        start = i
        end = j
        while start < end:
            ip_list[start], ip_list[end] = ip_list[end], ip_list[start]
            start += 1
            end -= 1

        total_cost += j - i + 1

        if total_cost > cost:
            return False

    if total_cost == cost:
        return True
    return False


def main():
    t = int(input())
    for i in range(1, t + 1):
        n, cost = input().split(" ")
        ip_list = [i for i in range(1, int(n) + 1)]
        perms = permutations(ip_list, int(n))
        ip_list = None
        found = False
        for permutation in perms:
            is_match = reversort(list(permutation), int(cost))
            if is_match:
                found = True
                print(f'Case #{i}: {" ".join([str(p) for p in permutation])}')
                break

        if not found:
            print(f"Case #{i}: IMPOSSIBLE")


if __name__ == "__main__":
    main()
