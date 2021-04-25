def first_non_repeating_character(string):
    char_map = {}
    for count, char in enumerate(string):
        if char not in char_map:
            char_map[char] = [count]
        else:
            char_map[char].append(count)

    min_index = None
    for val in char_map.values():
        if len(val) == 1:
            if min_index is None or val[0] < min_index:
                min_index = val[0]
    if min_index is None:
        return "_"
    return string[min_index]


def first_non_repeating_character_v1(string):
    char_array = [0 for i in range(26)]
    char_map = {
        element: index
        for index, element in enumerate("abcdefghijklmnopqrstuvwxyz")
    }

    for count, char in enumerate(string):
        char_array[char_map[char]] += 1

    index_found = None
    for index, element in enumerate(char_array):
        if element == 1:
            index_found = index
            break

    if index_found is not None:
        for key, val in char_map.items():
            if val == index_found:
                return key

    return "_"


if __name__ == "__main__":
    string = "abcebcft"
    print(first_non_repeating_character(string))

    string = "abcebcft"
    print(first_non_repeating_character_v1(string))
