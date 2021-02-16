import os


class _Node:
    '''
    Creates a Node with three fields:
    1. element (accessed using ._element)
    2. link (accessed using ._link)
    3. prev (accessed using ._prev)
    '''
    __slots__ = '_element', '_link', '_prev'

    def __init__(self, element, link, prev):
        '''
        Initialses _element, _link and _prev with element, link and prev respectively.
        '''
        self._element = element
        self._link = link
        self._prev = prev


class DoublyLL:
    '''
    Consists of member funtions to perform different
    operations on the doubly linked list.
    '''

    def __init__(self):
        '''
        Initialises head, tail and size with None, None and 0 respectively.
        '''
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        '''
        Returns length of linked list
        '''
        return self._size

    def isempty(self):
        '''
        Returns True if doubly linked list is empty, otherwise False.
        '''
        return self._size == 0

    def addLast(self, e):
        '''
        Adds the passed element at the end of the doubly linked list.
        '''
        newest = _Node(e, None, None)

        if self.isempty():
            self._head = newest
        else:
            self._tail._link = newest
            newest._prev = self._tail
        self._tail = newest
        self._size += 1

    def addFirst(self, e):
        '''
        Adds the passed element at the beginning of the doubly linked list.
        '''
        newest = _Node(e, None, None)

        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            newest._link = self._head
            self._head._prev = newest
        self._head = newest
        self._size += 1

    def addAnywhere(self, e, index):
        '''
        Adds the passed element at the passed index position of the doubly linked list.
        '''
        if index >= self._size:
            print(
                f'Index value out of range, it should be between 0 - {self._size - 1}')
        elif self.isempty():
            print("List was empty, item will be added at the end")
            self.addLast(e)
        elif index == 0:
            self.addFirst(e)
        elif index == self._size - 1:
            self.addLast(e)
        else:
            newest = _Node(e, None, None)
            p = self._head
            for _ in range(index - 1):
                p = p._link
            newest._link = p._link
            p._link._prev = newest
            newest._prev = p
            p._link = newest
            self._size += 1

    def removeFirst(self):
        '''
        Removes element from the beginning of the doubly linked list.
        Returns the removed element.
        '''
        if self.isempty():
            print('List is already empty')
            return
        e = self._head._element
        self._head = self._head._link
        self._size -= 1

        if self.isempty():
            self._tail = None
        else:
            self._head._prev = None
        return e

    def removeLast(self):
        '''
        Removes element from the end of the doubly linked list.
        Returns the removed element.
        '''
        if self.isempty():
            print("List is already empty")
            return
        e = self._tail._element
        self._tail = self._tail._prev
        self._size -= 1

        if self.isempty():
            self._head = None
        else:
            self._tail._link = None

        return e

    def removeAnywhere(self, index):
        '''
        Removes element from the passed index position of the doubly linked list.
        Returns the removed element.
        '''
        if index >= self._size:
            print(
                f'Index value out of range, it should be between 0 - {self._size - 1}')
        elif self.isempty():
            print("List is empty")
        elif index == 0:
            return self.removeFirst()
        elif index == self._size - 1:
            return self.removeLast()
        else:
            p = self._head
            for _ in range(index - 1):
                p = p._link
            e = p._link._element
            p._link = p._link._link
            p._link._prev = p
            self._size -= 1
        return e

    def display(self):
        '''
        Utility function to display the doubly linked list in
        both the directions i.e. forward and reverse.
        '''
        if self.isempty():
            print("List is Empty")
            return

        print("Forward direction")
        p = self._head
        print("NULL<-->", end='')
        while p:
            print(p._element, end="<-->")
            p = p._link
        print("NULL")

        print("\nReverse direction")
        p = self._tail
        print("NULL<-->", end='')
        while p:
            print(p._element, end="<-->")
            p = p._prev
        print("NULL")

        print(
            f"\nHead : {self._head._element}, Tail : {self._tail._element}")

###############################################################################


def options():
    '''
    Prints Menu for operations
    '''
    options_list = ['Add Last', 'Add First', 'Add Anywhere',
                    'Remove First', 'Remove Last', 'Remove Anywhere',
                    'Display List', 'Exit']

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
        elem = int(input("Enter Item: "))
        DL.addLast(elem)
        print("Added Item at Last!\n\n")

    elif choice == 2:
        elem = int(input("Enter Item: "))
        DL.addFirst(elem)
        print("Added Item at First!\n\n")

    elif choice == 3:
        elem = int(input("Enter Item: "))
        index = int(input("Enter Index: "))
        DL.addAnywhere(elem, index)

    elif choice == 4:
        print("Removed Element from First:", DL.removeFirst())

    elif choice == 5:
        print("Removed Element from last:", DL.removeLast())

    elif choice == 6:
        index = int(input("Enter Index: "))
        print(f"Removed Item: {DL.removeAnywhere(index)} !\n\n")

    elif choice == 7:
        print("List:")
        DL.display()
        print("\n")

    elif choice == 8:
        import sys
        sys.exit()

###############################################################################


if __name__ == '__main__':
    DL = DoublyLL()
    while True:
        choice = options()
        switch_case(choice)
