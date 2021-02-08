def sumofN(n):
    if n == 1:
        return n
    else:
        return sumofN(n-1) + n

print(sumofN(5))