def bubble(A):
    n = len(A)

    for passes in range(n - 1, 0, -1):
        for i in range(passes):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]


if __name__ == '__main__':
    A = [4, 3, 5, 8, 9, 6, 2, -3, 0, 1]
    # A = []
    # A = [0, -1]
    A = [1, 2, 3, 5, 6]
    print(A)
    bubble(A)
    print(A)
