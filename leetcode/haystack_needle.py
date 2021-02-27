class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == "" and needle == "":
            return 0

        if len(haystack) > 0 and needle == "":
            return 0

        needle_length = len(needle)
        needle_index = 0
        index_found = -1

        needle_dict = {}
        for needl in needle:
            if needl not in needle_dict:
                needle_dict[needl] = 1
            else:
                needle_dict[needl] += 1
        print(needle_dict)
        for count, ch in enumerate(haystack):
            # print(ch, needle_index)
            val = needle_dict.get(ch, 0)
            if val != 0:
                needle_dict[ch] -= 1
                if index_found == -1:
                    index_found = count
                # needle = needle[needle_count:]
                needle_index += 1
                if needle_dict[ch] == 0:
                    del needle_dict[ch]

                if needle_dict == {}:
                    return (count + 1) - needle_length
            else:
                index_found = -1
                needle_index = 0
        if needle_index != needle_length:
            return -1

        return index_found

    # if (haystack == "" and needle == "") or (len(haystack) > 0 and needle == "") or (
    #         len(haystack) == 1 and len(needle) == 1):
    #     return 0
    #
    # index_found = -1
    # needle_length = 0
    # st = 0
    # for i in range(len(haystack)):
    #
    #     for j in range(st, len(needle)):
    #         if needle[j] == haystack[i]:
    #             print(needle[j], haystack[i], i, j)
    #             needle_length += 1
    #             st += 1
    #         else:
    #             needle_length = 0
    #         break
    #     print("needle length", needle_length)
    #     if needle_length == len(needle):
    #         print(needle_length, len(needle), i)
    #         index_found = i - len(needle)
    #         return index_found
    #
    # if needle_length == len(needle):
    #     print(needle_length, len(needle), i)
    #     if i > 1:
    #         index_found = i - len(needle)
    #     else:
    #         index_found = i
    #
    # return index_found
