def pattern(n):
    [print(" "*(n-i), "*"*i, "*"*(i-1), sep="") for i in range(1, n +1)]
    

pattern(5)