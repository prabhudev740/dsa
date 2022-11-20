def search(A, key):
    start = 0
    end = len(A) - 1

    while start <= end:
        mid = (start + end) // 2

        if A[mid] == key:
            return mid

        elif A[mid] > key:
            start = mid + 1

        else:
            end = mid - 1

    return -1


if __name__ == '__main__':
    A = [-1, 0, 3, 11, 15]
    # A = [-1]
    # A = []
    A.reverse()
    key = 3
    # key = 1
    res = search(A, key)
    print(res)
