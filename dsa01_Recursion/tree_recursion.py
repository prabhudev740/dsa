def sol(n):
    if n > 0:
        sol(n - 1)
        print(n)
        sol(n - 1)


sol(5)