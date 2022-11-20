def selection(A):
    n = len(A)

    for i in range(n):
        pos = i

        for j in range(i+1, n):
            if A[j] < A[pos]:
                pos = j

        A[i], A[pos] = A[pos], A[i]


if __name__ == "__main__":
    A = [ 2, 5, 3, 1, 4]
    A = []
    A = [1]
    A = [-1, -5, -3, 0, 10]
    print(A)
    selection(A)
    print(A)
