class Heap:
    def __init__(self, maxsize):
        '''
        Initialises the size of heap using maxsize parameter passed by users.
        '''
        self._maxsize = maxsize
        self._heap = [-1] * (self._maxsize + 1)
        self._size = 0
        self._type = 'Max'

    def __len__(self):
        '''
        Returns the size of heap.
        '''
        return self._size

    def isempty(self):
        '''
        Returns True if heap is empty, else False.
        '''
        return self._size == 0

    def insert(self, e, max=True):
        '''
        Insertion Operation for creating a Max Heap(Min Heap if max = False)
        '''
        if self._size == self._maxsize:
            print(f"Max {self._maxsize} elements can be inserted !")
        else:
            self._size += 1
            hi = self._size

            if max:
                # while child > parent -- Max Heap
                while e > self._heap[hi//2] and hi > 1:
                    self._heap[hi] = self._heap[hi//2]
                    hi = hi//2
            else:
                self._type = 'Min'
                # while child < parent -- Min Heap
                while e < self._heap[hi//2] and hi > 1:
                    self._heap[hi] = self._heap[hi//2]
                    hi = hi//2
            self._heap[hi] = e

    def returnRoot(self):
        '''
        Returns the root element from the heap.
        Maximum element if it was a Max heap, Minimum otherwise.
        '''
        return self._type , self._heap[1]

    def deleteMax(self):
        '''
        Deletes the maximum element from the heap.
        '''
        root = self._heap[1]
        self._heap[1] = self._heap[self._size]
        self._heap[self._size] = -1
        self._size -= 1

        i = 1
        j = i * 2
        while j <= self._size:
            if self._heap[j] < self._heap[j + 1]:
                j = j + 1
            if self._heap[i] < self._heap[j]:
                self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
                i = j
                j = i * 2
            else:
                break
        return root

    def display(self):
        '''
        Utility function to display the heap.
        '''
        if self.isempty():
            print("Heap is empty !")
        else:
            print("Heap: ", end='')
            for i in range(1, self._size + 1):
                print(self._heap[i], end=" ")


def options():
    '''
    Prints Menu for operations
    '''
    options_list = ['Insert an item [Max]', 'Insert multiple items [Max]',
                    'Insert an item [Min]', 'Insert multiple items [Min]',
                    'Maximum / Minimum', 'Delete Max', 'Display', 'Exit']

    print("\nMENU")
    for i, option in enumerate(options_list):
        print(f'{i + 1}. {option}')

    choice = int(input("Enter choice: "))
    return choice

###############################################################################


def switch_case(choice):
    '''
    Switch Case for operations
    '''
    # os.system('cls')
    if choice == 1:
        elem = int(input("Enter an Item: "))
        hp.insert(elem)
    elif choice == 2:
        A = list(map(int, input("Enter items: ").split()))
        for elem in A:
            hp.insert(elem)

    elif choice == 3:
        elem = int(input("Enter an Item: "))
        hp.insert(elem, max=False)

    elif choice == 4:
        A = list(map(int, input("Enter items: ").split()))
        for elem in A:
            hp.insert(elem, max=False)

    elif choice == 5:
        heapType, value = hp.returnRoot()
        print(f"{heapType} element is: {value}")

    elif choice == 6:
        print("Deleted element is: ", hp.deleteMax())

    elif choice == 7:
        hp.display()

    elif choice == 8:
        import sys
        sys.exit()

###############################################################################


if __name__ == '__main__':
    hp = Heap(10)
    while True:
        choice = options()
        switch_case(choice)
