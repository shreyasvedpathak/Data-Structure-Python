def selection(A):
    """
    Algo name: Selection Sort
    UNSTABLE
    input:
    A -- Array

    returns sorted array
    """
    n = len(A)
    for i in range(n-1):
        position = i
        for j in range(i + 1, n):
            if A[j] < A[position]:
                position = j
        A[i], A[position] = A[position], A[i]
    print("Sorted using Selection Sort: ", A)

def insertion(A):
    """
    Algo name: Insertion Sort
    STABLE
    input:
    A -- Array

    returns sorted array
    """
    n = len(A)

    for i in range(1, n):
        cvalue = A[i]
        position = i
        while position > 0 and A[position - 1] > cvalue:
            A[position] = A[position - 1]
            position = position - 1
        A[position] = cvalue
    
    print("Sorted using Insertion Sort: ", A)

def switch_case(choice):
    if choice == 1:
        selection(A),
    elif choice == 2: 
        insertion(A)


A = list(map(int, input("Enter Array elements: ").split()))

print("Select Sorting Method")
print("1. Selection Sort")
print("2. Insertion Sort")

choice = int(input("Enter your choice: "))
switch_case(choice)
