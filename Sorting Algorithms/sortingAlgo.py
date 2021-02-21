import time
import random


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


def merge_driver(A):
    mergesort(A, 0, len(A)-1)

###############################################################


def partition(A, low, high):
    pivot = A[low]
    i = low + 1
    j = high

    while True:
        while i <= j and A[i] <= pivot:
            i = i + 1
        while i <= j and A[i] > pivot:
            j = j - 1

        if i <= j:
            A[i], A[j] = A[j], A[i]
        else:
            break
    A[low], A[j] = A[j], A[low]
    return j


def quicksort(A, low, high):
    """
    Algo name: Quick Sort
    UNSTABLE
    input:
    A -- Array
    left -- first index position of the array(0 in first call)
    right -- last index position of the array(len(A) - 1 in the first call)

    """
    if low < high:
        p = partition(A, low, high)
        quicksort(A, low, p - 1)
        quicksort(A, p + 1, high)


def quick_driver(A):
    quicksort(A, 0, len(A)-1)

###############################################################


def count(A):
    """
    Algo name: Count Sort
    STABLE
    input:
    A -- Array
    returns sorted array
    """
    n = len(A)
    maxsize = max(A)
    carray = [0] * (maxsize + 1)

    for i in range(n):
        carray[A[i]] = carray[A[i]] + 1
    i = 0
    j = 0
    while i < maxsize + 1:
        if carray[i] > 0:
            A[j] = i
            j = j + 1
            carray[i] = carray[i] - 1
        else:
            i = i + 1

###############################################################


def radix(A):
    """
    Algo name: Radix Sort
    STABLE
    input:
    A -- Array
    returns sorted array
    """
    n = len(A)
    maxelement = max(A)
    digits = len(str(maxelement))
    l = []
    bins = [l] * 10
    for i in range(digits):
        for j in range(n):
            e = int((A[j] / pow(10, i)) % 10)
            if len(bins[e]) > 0:
                bins[e].append(A[j])
            else:
                bins[e] = [A[j]]
        k = 0
        for x in range(10):
            if len(bins[x]) > 0:
                for y in range(len(bins[x])):
                    A[k] = bins[x].pop(0)
                    k = k + 1

###############################################################


def heapsort(A):
    """
    Algo name: Heap Sort
    UNSTABLE
    input:
    A -- Array
    returns sorted array
    """
    import sys
    sys.path.append('.')
    from Heap.heap import Heap

    n = len(A)
    heap = Heap(n)
    for i in range(n):
        heap.insert(A[i])
    k = n - 1
    for _ in range(heap._size):
        A[k] = heap.deleteMax()
        k -= 1

###############################################################


def bucket(A):
    """
    Algo name: Bucket Sort
    STABLE
    input:
    A -- Array
    returns sorted array
    """
    n = len(A)
    maximum = max(A)
    l = []
    buckets = [l] * 10
    for i in range(n):
        index = int((n * A[i]) / (maximum + 1))
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

###############################################################


def timereq(choices, algo_name):
    """
    Utility function to calculate time required(in nanoseconds) to sort the given array.
    """
    for c, name in zip(choices, algo_name):
        start = time.time()
        c(A)
        end = time.time()
        print('Time taken by', name, ':', (end - start) * 10 ** 6, "nanoseconds")

###############################################################


def create_array():
    """
    Return randomly generates an integer array having limit as upper limit
    and amount as length of the array
    """
    limit = int(input("Enter the upper limit for generating the numbers: "))
    amount = int(input("Enter the amount of numbers you want to generate: "))
    print("Generating numbers...\n")
    array = []
    for i in range(amount):
        n = random.randint(0, limit)
        array.append(n)
    return array

###############################################################


def options():
    '''
    Prints Menu for operations
    '''
    options_list = ['Selection Sort', 'Insertion Sort', 'Bubble Sort', 'Shell Sort',
                    'Merge Sort', 'Quick Sort', 'Count Sort', 'Radix Sort', 'Heap Sort',
                    'Bucket Sort', 'Time Required', 'Exit']
    print("MENU")
    for i, option in enumerate(options_list):
        print(f'{i + 1}. {option}')


def switch_case(choice):
    choices = [selection, insertion, bubble, shell, merge_driver,
               quick_driver, count, radix, heapsort, bucket]
    algo_name = ['Selection Sort', 'Insertion Sort', 'Bubble Sort', 'Shell Sort', 'Merge Sort',
                 'Quick Sort', 'Count Sort', 'Radix Sort', 'Heap Sort', 'Bucket Sort']

    if choice != 11:
        choices[choice-1](A)
        print("Sorted using", algo_name[choice - 1], "\n", A)
    else:
        timereq(choices, algo_name)


###############################################################
if __name__ == '__main__':
    while True:
        x = input("Enter your own array values? [y/n]: ")
        if x == 'y':
            A = list(map(int, input("Enter values: ").split()))
            options()
        else:
            A = create_array()
            options()

        choice = int(input("Enter your choice: "))
        if choice != 12:
            switch_case(choice)
        else:
            break
