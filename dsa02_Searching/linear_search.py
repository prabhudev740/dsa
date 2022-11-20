def search(A, key):
    n = len(A)

    for index, val in enumerate(A):
        if val == key:
            return index

    return -1


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    res = search(A, 5)
    print(res)