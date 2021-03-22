from queue_test import Queue


def first_non_repeating(str):
    q = Queue()
    map = dict()
    for ch in str:
        if ch not in map:
            map[ch] = 1
            q.enqueue(ch)
        else:
            map[ch] += 1
            if q.current_queue_element() == ch:
                q.dequeue()
    element = q.current_queue_element()
    if map.get(element) and map.get(element) > 1:
        return -1
    return element


if __name__ == "__main__":
    str = "abacc"
    print(first_non_repeating(str))

    str = "ab"
    print(first_non_repeating(str))
