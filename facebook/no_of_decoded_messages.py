"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

"ab" -> "12"
"l" -> "12"
"""


def helper(data, k):
    if k == 0:
        return 1
    s = len(data) - k
    if data[s] == "0":
        return 0
    result = helper(data, k - 1)
    if k >= 2 and int(data[s : s + 2]) <= 26:
        result += helper(data, k - 2)
    return result


def no_of_decoded_messages(encoded_message):
    return helper(encoded_message, len(encoded_message))


# Dynamic programming memoization
def helper_v1(data, k, memo):
    if k == 0:
        return 1
    s = len(data) - k
    if data[s] == "0":
        return 0
    if k in memo and memo[k] is not None:
        return memo[k]

    result = helper_v1(data, k - 1, memo)
    if k >= 2 and int(data[s : s + 2]) <= 26:
        result += helper_v1(data, k - 2, memo)
    memo[k] = result
    return result


def no_of_decoded_messages_v1(encoded_message):
    memo = [None for i in range(len(encoded_message) + 1)]
    return helper_v1(encoded_message, len(encoded_message), memo)


if __name__ == "__main__":
    data = "3"
    print(no_of_decoded_messages(data))

    data = "12"
    print(no_of_decoded_messages(data))

    data = "26"
    print(no_of_decoded_messages(data))

    data = "111"
    print(no_of_decoded_messages(data))

    data = "3"
    print(no_of_decoded_messages_v1(data))

    data = "12"
    print(no_of_decoded_messages_v1(data))

    data = "26"
    print(no_of_decoded_messages_v1(data))

    data = "111"
    print(no_of_decoded_messages_v1(data))
