def factorialofN(n):
    if n == 0:
        return 1
    else:
        return factorialofN(n-1) * n

print(factorialofN(7))