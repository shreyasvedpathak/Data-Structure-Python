import math

def bs_itr(A, n, key):
    low = 0
    high = n - 1

    while low <= high:
        mid = math.floor((low + high)/2)

        if key == A[mid]:
            return mid
        elif key < A[mid]:
            high = mid - 1
        elif key > A[mid]:
            low = mid + 1

    return "Not Found"


A = [1, 2, 3, 4, 5, 6, 7]

print(A)
print("Iterative Binary Search output:", bs_itr(A, len(A), 10))
print("Iterative Binary Search output:", bs_itr(A, len(A), 5))
print("Iterative Binary Search output:", bs_itr(A, len(A), 2))


def bs_recur(A, key, low = 0, high = len(A) - 1):
    if low > high:
        return "Not Found"
    else:
        mid = math.floor((low + high)/2)

        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return bs_recur(A, key, low, mid - 1)
        elif key > A[mid]:
            return bs_recur(A, key, mid + 1, high)


print("Recursive Binary Search output:", bs_recur(A, 10))
print("Recursive Binary Search output:", bs_recur(A, 5))
print("Recursive Binary Search output:", bs_recur(A, 2))