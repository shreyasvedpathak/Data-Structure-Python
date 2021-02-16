import os


class _Node:
    '''
    Creates a Node with two fields:
    1. element (accesed using ._element)
    2. link (accesed using ._link)
    '''
    __slots__ = '_element', '_link'

    def __init__(self, element, link):
        '''
        Initialses _element and _link with element and link respectively.
        '''
        self._element = element
        self._link = link


class QueueLL:
    '''
    Consists of member funtions to perform different
    operations on the linked list.
    '''

    def __init__(self):
        '''
        Initialses head, tail and size with None, None and 0 respectively.
        '''
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        '''
        Returns length of Queue
        '''
        return self._size

    def isempty(self):
        '''
        Returns True if Queue is empty, otherwise False.
        '''
        return self._size == 0

    def enqueue(self, e):
        '''
        Adds the passed element at the end of the linked list.
        That means, it enqueues element.
        '''
        newest = _Node(e, None)

        if self.isempty():
            self._head = newest
        else:
            self._tail._link = newest

        self._tail = newest
        self._size += 1

    def dequeue(self):
        '''
        Removes element from the beginning of the linked list and 
        returns the removed element.
        That means, it dequeues.
        '''
        if self.isempty():
            print("Queue is Empty. Cannot perform dequeue operation.")
            return

        e = self._head._element
        self._head = self._head._link
        self._size = self._size - 1

        if self.isempty():
            self._tail = None
        return e

    def first(self):
        '''
        Peeks and return the first element in the Queue.
        '''
        if self.isempty():
            print("Queue is Empty.")
            return
        e = self._head._element
        return e

    def display(self):
        '''
        Utility function to display the Queue.
        '''
        if self.isempty() == 0:
            p = self._head
            print("Front", end=' <--')
            while p:
                print(p._element, end='<--')
                p = p._link
            print(" Rear")
        else:
            print("Empty")

###############################################################################


def options():
    '''
    Prints Menu for operations
    '''
    options_list = ['Enqueue', 'Dequeue', 'First',
                    'Display Queue', 'Exit']

    print("MENU")
    for i, option in enumerate(options_list):
        print(f'{i + 1}. {option}')

    choice = int(input("Enter choice: "))
    return choice


def switch_case(choice):
    '''
    Switch Case for operations
    '''
    os.system('cls')
    if choice == 1:
        elem = int(input("Enter item to Enqueue: "))
        Q.enqueue(elem)

    elif choice == 2:
        print('Dequeued item is: ', Q.dequeue())

    elif choice == 3:
        print("First item is: ", Q.first())

    elif choice == 4:
        print("Queue: ")
        Q.display()
        print("\n")

    elif choice == 5:
        import sys
        sys.exit()

###############################################################################


if __name__ == '__main__':
    Q = QueueLL()
    while True:
        choice = options()
        switch_case(choice)
