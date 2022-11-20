def mergesort(A, left, right):
    if left < right:
        mid = (left + right) // 2

        mergesort(A, left, mid)
        mergesort(A, mid + 1, right)

        merge(A, left, mid, right)


def merge(A, left, mid, right):
    i, j = left, mid + 1
    B = []

    while i <= mid and j <= right:
        if A[i] < A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1

    if i <= mid:
        B.extend(A[i:mid + 1])

    if j <= right:
        B.extend(A[j:right + 1])

    for x, v in enumerate(B):
        A[left + x] = v


if __name__ == '__main__':
    A = [3, 5, 8, 9, 6, 2]
    print(A)
    mergesort(A, 0, len(A) - 1)
    print(A)
