import os
from typing import Sized

class _Node:
    __slots__ = '_element', '_link'

    def __init__(self, element, link):
        self._element = element
        self._link = link

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0
    
    def addLast(self, e):
        newest = _Node(e,None)

        if self.isempty():
            self._head = newest
        else:
            self._tail._link = newest

        self._tail = newest
        self._size += 1

    def addFirst(self, e):

        newest = _Node(e, None)

        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            newest._link = self._head
            self._head = newest
        self._size += 1

    def addAnywhere(self, e, index):

        newest = _Node(e, None)

        i = index - 1
        p = self._head

        if self.isempty():
            self.addFirst(e)
        else:
            for i in range(i):
                p = p._link
            newest._link = p._link
            p._link = newest
        self._size += 1

    def display(self):
        if self.isempty() == 0:
            p = self._head
            while p:
                print(p._element, end='-->')
                p = p._link
            print("NULL")
        else:
            print("List is Empty")

    def search(self, key):
        p = self._head
        index = 0
        while p:
            if p._element == key:
                return index
            p = p._link
            index += 1
        return -1

###############################################################################

def options():
    options_list = ['Add item', 'Add First', 'Add Anywhere', 'Display List', 'Print Size', 'Search', 'Exit']

    print("MENU")
    for i, option in enumerate(options_list):
        print(f'{i + 1}. {option}')    

    choice = int(input("Enter choice: "))
    return choice

def switch_case(choice):

    os.system('cls')
    if choice == 1:
        elem = int(input("Enter Item: "))
        L.addLast(elem)
        print("Added Item at Last!\n\n")
    elif choice == 2:
        elem = int(input("Enter Item: "))
        L.addFirst(elem)
        print("Added Item at First!\n\n")
    elif choice == 3:
        elem = int(input("Enter Item: "))
        index = int(input("Enter Index: "))
        L.addAnywhere(elem, index)
        print(f"Added Item at index {index}!\n\n")
    elif choice == 4:
        print("List: ", end='')
        L.display()
        print("\n")
    elif choice == 5:
        print("Size:", len(L))
        print("\n")
    elif choice == 6:
        key = int(input("Enter item to search: "))
        if L.search(key) >= 0:
            print(f"Item {key} found at index position {L.search(key)}\n\n")
        else:
            print("Item not in the list\n\n")

    elif choice == 7:
        exit


L = LinkedList()
while True:
    choice = options()
    switch_case(choice)
