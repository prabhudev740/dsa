def sol(n):
    if n > 0:
        print(n)
        sol(n - 1)

sol(10)