def shell(A):
    n = len(A)
    gap = n // 2

    while gap:
        for i in range(gap, n):
            temp = A[i]
            j = i - gap
            while j >= 0 and A[j] > temp:
                A[j + gap] = A[j]
                j -= gap

            A[j + gap] = temp

        gap //= 2


if __name__ == '__main__':
    A = [3, 5, 8, 9, 6, 2]
    print(A)
    shell(A)
    print(A)
