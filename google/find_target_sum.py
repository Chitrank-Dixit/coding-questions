"""
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""


def find_match_v1(elment_sum, list_of_nums):
    for i in range(len(list_of_nums)):
        for j in range(len(list_of_nums)):
            if i != j:
                if list_of_nums[i] + list_of_nums[j] == elment_sum:
                    return True
    return False


def find_match_v2(element_sum, list_of_nums):
    num_dict = dict()
    for e in list_of_nums:
        if e in num_dict:
            return True
        num_dict[element_sum - e] = e
    return False


if __name__ == "__main__":
    element_sum = 25
    list_of_nums = li = [10, 15, 3, 7]
    print(find_match_v2(element_sum=element_sum, list_of_nums=list_of_nums))
