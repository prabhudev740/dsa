def search(A, key, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if A[mid] == key:
        return mid

    elif A[mid] > key:
        return search(A, key, start, mid - 1)

    else:
        return search(A, key, mid + 1, end)


if __name__ == '__main__':
    A = [-1, 0, 3, 11, 15]
    # A = [-1]
    A = []
    key = 0
    # key = 1
    res = search(A, key, 0, len(A) -1)
    print(res)
