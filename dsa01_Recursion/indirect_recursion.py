def sol1(n):
    if n > 0:
        print(n)
        sol2(n - 1)

def sol2(n):
    if n > 0:
        print(n)
        sol1(n - 1)


sol1(5)