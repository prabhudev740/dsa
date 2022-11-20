def insertion(A):
    n = len(A)

    for i in range(1, n):
        current = A[i]
        pos = i

        while pos > 0 and A[pos - 1] > current:
            A[pos] = A[pos - 1]
            pos -= 1

        A[pos] = current


if __name__ == '__main__':
    A = [3, 5, 8, 9, 6, 2]
    print(A)
    insertion(A)
    print(A)
