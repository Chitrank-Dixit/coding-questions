

def shortest_substring(s, c, k):
    list_of_strings = []
    found = False
    string = ""
    tl = 0
    for i, element in enumerate(s):
        if element == c:
            tl = k
            string = c
            found = True
            tl -= 1
        if found == True:
            for j in range(i + 1, len(s)):
                if tl == 0:
                    break
                if tl > 0:
                    string += s[j]
                if s[j] == c:
                    tl -= 1
            list_of_strings.append(string)
            tl = k
    min_len = len(list_of_strings[0])

    for ele in list_of_strings:
        if len(ele) < min_len:
            min_len = len(ele)
    return min_len


if __name__ == "__main__":
    s = "apple"
    c = "p"
    k = 2
    print(shortest_substring(s, c, k))