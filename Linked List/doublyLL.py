import os
from typing import NewType, Sized

class _Node:
    __slots__ = '_element', '_link', '_prev'
    def __init__(self, element, link, prev):
        self._element = element
        self._link = link
        self._prev = prev
    
class DoublyLL:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def isempty(self):
        return self._size == 0

    def addLast(self, e):
        newest = _Node(e, None, None)

        if self.isempty():
            self._head = newest
        else:
            self._tail._link = newest
            newest._prev = self._tail
        self._tail = newest
        self._size += 1

    def addFirst(self, e):
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
        if index >= self._size:
            print(f'Index value out of range, it should be between 0 - {self._size - 1}')
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


    def display(self):
        if self.isempty():
            print("List is Empty")
            return
        
        p = self._head
        print("NULL<-->", end='')
        while p:
            print(p._element, end="<-->")
            p = p._link
        print("NULL")
        print(
            f"Head : {self._head._element}, Tail : {self._tail._element}")

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
        print("List: ", end='')
        DL.display()
        print("\n")

    elif choice == 8:
        import sys
        sys.exit()

###############################################################################


DL = DoublyLL()
while True:
    choice = options()
    switch_case(choice)
