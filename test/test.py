n = int(input())

arr = sorted(list(map(int, input().split())))

res = 0

for i in range(2, n*2, 2):
    res += arr[i+1] - arr[i]

print(res)

def result():
    a = []
    n = int(input())
    for i in range(n):
        a.append(int(input()))

    a.sort()

    if len(a) != len(set(a)):
        return False

    for i, v in enumerate(a[:n-1]):
        flag = True
        for x in a[i+1:]:
            if x % v == 0:
                flag = False
                break
        if flag:
            return False

    return True


if result():
    print("Yes")
else:
    print("No")



arr = []
n = int(input())

for i in range(n):
    arr.append(int(input()))

temp = []

for i in range(1, n-1):
    if arr[i-1] > arr[i+1]:
        temp.append(arr[i-1])
    else:
        temp.append(arr[i+1])

print("".join(map(str, temp)))



n = int(input())

even = odd = []

for i in range(1, n + 1):
    if not n % i:
        if n % 2:
            odd.append(i)
        else:
            even.append(i)

if len(odd) > len(even):
    print(1)
else:
    print(0)