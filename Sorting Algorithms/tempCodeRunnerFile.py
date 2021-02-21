    n = len(A)
    maximum = max(A)
    l = []
    buckets = [l] * 10
    for i in range(n):
        index = int(n * A[i] / (maximum + 1))
        if len(buckets[index]) == 0:
            buckets[index] = [A[i]]
        else:
            buckets[index].append(A[i])
    for i in range(10):
        insertion(buckets[i])
    k = 0
    for i in range(10):
        for j in range(len(buckets[i])):
            A[k] = buckets[i].pop(0)
            k = k + 1