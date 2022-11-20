def countsort(A):
    n = len(A)
    maxsize = max(A) + 1
    temp = [0] * maxsize

    for i in A:
        temp[i] += 1

    i = j = 0
    while i < maxsize:
        if temp[i]:
            A[j] = i
            j += 1
            temp[i] -= 1
        else:
            i += 1

    # j = 0
    # for i, v in enumerate(temp):
    #     while v:
    #         A[j] = i
    #         v -= 1
    #         j += 1


if __name__ == '__main__':
    A = [5, 3, 2, 1, 4, 5, 3, 5]
    print(A)
    countsort(A)
    print(A)