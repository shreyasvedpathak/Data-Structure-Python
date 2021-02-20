import os
from typing import NewType


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


class LinkedList:
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
        Returns length of linked list
        '''
        return self._size

    def isempty(self):
        '''
        Returns True if linked list is empty, otherwise False.
        '''
        return self._size == 0

    def addLast(self, e):
        '''
        Adds the passed element at the end of the linked list.
        '''
        newest = _Node(e, None)

        if self.isempty():
            self._head = newest
        else:
            self._tail._link = newest

        self._tail = newest
        self._size += 1

    def addFirst(self, e):
        '''
        Adds the passed element at the beginning of the linked list.
        '''
        newest = _Node(e, None)

        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            newest._link = self._head
            self._head = newest
        self._size += 1

    def addAnywhere(self, e, index):
        '''
        Adds the passed element at the passed index position of the linked list.
        '''
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
            print(f"Added Item at index {index}!\n\n")
        self._size += 1

    def addSorted(self, e):
        '''
        Adds passed element at a position that making linked list sorted.
        '''
        newest = _Node(e, None)

        if self.isempty():
            self.addFirst(e)
        else:
            curr = prev = self._head
            while curr and curr._element < e:
                prev = curr
                curr = curr._link
            # if no element is found to be smaller than e, curr will point to head.
            # that means, it should be the first element.
            if curr == self._head:
                self.addFirst(e)
            else:
                newest._link = prev._link
                prev._link = newest
                self._size += 1


    def removeFirst(self):
        '''
        Removes element from the beginning of the linked list.
        Returns the removed element.
        '''
        if self.isempty():
            print("List is Empty. Cannot perform deletion operation.")
            return

        e = self._head._element
        self._head = self._head._link
        self._size = self._size - 1

        if self.isempty():
            self._tail = None

        return e

    def removeLast(self):
        '''
        Removes element from the end of the linked list.
        Returns the removed element.
        '''
        if self.isempty():
            print("List is Empty. Cannot perform deletion operation.")
            return

        p = self._head
        if p._link == None:
            e = p._element
            self._head = None
        else:
            while p._link._link != None:
                p = p._link
            e = p._link._element
            p._link = None
            self._tail = p

        self._size = self._size - 1
        return e

    def removeAnywhere(self, index):
        '''
        Removes element from the passed index position of the linked list.
        Returns the removed element.
        '''
        p = self._head
        i = index - 1

        if index == 0:
            return self.removeFirst()
        elif index == self._size - 1:
            return self.removeLast()
        else:
            for x in range(i):
                p = p._link
            e = p._link._element
            p._link = p._link._link

        self._size -= 1
        return e

    def display(self):
        '''
        Utility function to display the linked list.
        '''
        if self.isempty() == 0:
            p = self._head
            while p:
                print(p._element, end='-->')
                p = p._link
            print("NULL")
        else:
            print("Empty")

    def search(self, key):
        '''
        Searches for the passed element in the linked list.
        Returns the index position if found, else -1.
        '''
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
    '''
    Prints Menu for operations
    '''
    options_list = ['Add Last', 'Add First', 'Add Anywhere', 'Insert Sorted',
                    'Remove First', 'Remove Last', 'Remove Anywhere',
                    'Display List', 'Print Size', 'Search', 'Exit']

    print("MENU")
    for i, option in enumerate(options_list):
        print(f'{i + 1}. {option}')

    choice = int(input("Enter choice: "))
    return choice


def switch_case(choice):
    '''
    Switch Case for operations
    '''
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

    elif choice == 4:
        elem = int(input("Enter Item: "))
        L.addSorted(elem)

    elif choice == 5:
        print("Removed Element from First:", L.removeFirst())

    elif choice == 6:
        print("Removed Element from last:", L.removeLast())

    elif choice == 7:
        index = int(input("Enter Index: "))
        print(f"Removed Item: {L.removeAnywhere(index)} !\n\n")
    elif choice == 8:
        print("List: ", end='')
        L.display()
        print("\n")

    elif choice == 9:
        print("Size:", len(L))
        print("\n")

    elif choice == 10:
        key = int(input("Enter item to search: "))
        if L.search(key) >= 0:
            print(f"Item {key} found at index position {L.search(key)}\n\n")
        else:
            print("Item not in the list\n\n")

    elif choice == 11:
        import sys
        sys.exit()

###############################################################################


if __name__ == '__main__':
    L = LinkedList()
    while True:
        choice = options()
        switch_case(choice)
