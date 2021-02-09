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

###############################################################

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

###############################################################

def bubble(A):
    """
    Algo name: Bubble Sort
    STABLE
    input:
    A -- Array

    returns sorted array
    """
    n = len(A)
    for p in range(n-1, 0, -1):
        for i in range(0, p):
            if A[i] > A[i + 1]:
                A[i], A[i+1] = A[i+1], A[i]
    print("Sorted using Bubble Sort: ", A)

###############################################################

def shell(A):
    """
    Algo name: Shell Sort
    UNSTABLE
    input:
    A -- Array

    returns sorted array
    """
    n = len(A)
    gap = n//2
    while gap > 0:
        i = gap
        while i < n:
            temp = A[i]
            j = i - gap
            while j >= 0 and A[j] > temp:
                A[j+gap] = A[j]
                j = j - gap
            A[j+gap] = temp
            i = i + 1
        gap = gap // 2
    print("Sorted using Shell Sort: ", A)

###############################################################

def merge(A, l, m, r):
    """
    Algo name: Merge
    input:
    A -- Array
    l -- first index position of the array
    m -- middle index postion of the array calculated
         using l and r
    r -- last index position of the array

    returns Sorted partial array A
    """

    i = l
    j = m + 1 
    k = l
    B = [0] * (r + 1)
    while i <= m and j <= r:
        if A[i] < A[j]:
            B[k] = A[i]
            i = i + 1
        else:
            B[k] = A[j]
            j = j + 1
        k = k + 1

    while i <= m:
        B[k] = A[i]
        i = i + 1
        k = k + 1
    while j <= r:
        B[k] = A[j]
        j = j + 1
        k = k + 1
    for x in range(l, r + 1):
        A[x] = B[x]


def mergesort(A, left, right):
    """
    Algo name: Merge Sort
    UNSTABLE
    input:
    A -- Array
    left -- first index position of the array(0 in first call)
    right -- last index position of the array(len(A) - 1 in the first call)

    """
    if left < right:
        mid = (left + right) // 2
        mergesort(A, left, mid)
        mergesort(A, mid + 1, right)
        merge(A, left, mid, right) 


###############################################################
def switch_case(choice):
    if choice == 1:
        selection(A),
    elif choice == 2: 
        insertion(A)
    elif choice == 3: 
        bubble(A)
    elif choice == 4: 
        shell(A)
    elif choice == 5:
        mergesort(A, 0, len(A)-1)
        print("Sorted using Merge Sort: ", A)

###############################################################

A = list(map(int, input("Enter Array elements: ").split()))

print("Select Sorting Method")
print("1. Selection Sort")
print("2. Insertion Sort")
print("3. Bubble Sort")
print("4. Shell Sort")
print("5. Merge Sort")

choice = int(input("Enter your choice: "))
switch_case(choice)
