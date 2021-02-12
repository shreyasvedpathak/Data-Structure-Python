import os

from typing_extensions import TypeAlias

class _Node:
    __slots__ = '_element', '_link'

    def __init__(self, element, link):
        self._element = element
        self._link = link

class CicularLL:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def addLast(self, e):
        newest = _Node(e, None)

        if self.isempty():
            self._head = newest
            newest._link = self._head
        else:
            newest._link = self._tail._link
            self._tail._link = newest
        
        self._tail = newest
        self._size += 1
    
    def addFirst(self, e):
        newest = _Node(e, None)

        if self.isempty():
            newest._link = self._head
            self._head = newest
            self._tail = newest
        else:
            newest._link = self._head
            self._tail._link = newest
            self._head = newest
        self._size += 1
            

    def display(self):
        if self.isempty() == 0:
            p = self._head
            while True:
                print(p._element, end='-->')
                p = p._link
                if p == self._head:
                    break
            print(f'({p._element} head)')
        else:
            print("Empty")

#########################################################################


def options():
    options_list = ['Add Last', 'Add First', 'Add Anywhere',
                    'Remove First', 'Remove Last', 'Remove Anywhere',
                    'Display List', 'Exit']

    print("MENU")
    for i, option in enumerate(options_list):
        print(f'{i + 1}. {option}')

    choice = int(input("Enter choice: "))
    return choice


def switch_case(choice):

    os.system('cls')
    if choice == 1:
        elem = int(input("Enter Item: "))
        CL.addLast(elem)
        print("Added Item at Last!\n\n")

    elif choice == 2:
        elem = int(input("Enter Item: "))
        CL.addFirst(elem)
        print("Added Item at First!\n\n")

    elif choice == 3:
        elem = int(input("Enter Item: "))
        index = int(input("Enter Index: "))
        CL.addAnywhere(elem, index)
        print(f"Added Item at index {index}!\n\n")

    elif choice == 4:
        print("Removed Element from First:", CL.removeFirst())

    elif choice == 5:
        print("Removed Element from last:", CL.removeLast())

    elif choice == 6:
        index = int(input("Enter Index: "))
        CL.removeAnywhere(index)
        print(f"Removed Item at index {index}!\n\n")
    elif choice == 7:
        print("List: ", end='')
        CL.display()
        print("\n")

    elif choice == 8:
        import sys
        sys.exit()


CL = CicularLL()
while True:
    choice = options()
    switch_case(choice)
