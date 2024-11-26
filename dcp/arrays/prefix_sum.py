def prefix_sum(arr):
    ps = list()
    ps.append(arr[0])
    for i in range(1, len(arr)):
        ps.append(arr[i] + ps[i-1])
    return ps

def get_sum(l, r):
    if l == 0:
        return ps[r]
    return ps[r] - ps[l-1]

def prefix_weigted_sum(arr):
    ps = list()
    ps.append(arr[0])
    for i in range(1, len(arr)):
        ps.append((i+1) * arr[i] + ps[i-1])
    return ps

def get_sum(l, r):
    if l == 0:
        return ps[r]
    return ps[r] - ps[l-1]

if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    ps = prefix_sum(arr)

    print(get_sum(0, 3))

    print(get_sum(1, 3 ))

    ps = prefix_weigted_sum(arr)
    print(get_sum(0, 3))

    print(get_sum(2, 3))
