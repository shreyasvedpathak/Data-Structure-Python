import os
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
        newest = _Node(e, None)

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

    def removeFirst(self):
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
        if self.isempty() == 0:
            p = self._head
            while p:
                print(p._element, end='-->')
                p = p._link
            print("NULL")
            print(
                f"Head : {self._head._element}, Tail : {self._tail._element}")
        else:
            print("Empty")

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
    options_list = ['Add Last', 'Add First', 'Add Anywhere',
                    'Remove First', 'Remove Last', 'Remove Anywhere',
                    'Display List', 'Print Size', 'Search', 'Exit']

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
        print("Removed Element from First:", L.removeFirst())

    elif choice == 5:
        print("Removed Element from last:", L.removeLast())

    elif choice == 6:
        index = int(input("Enter Index: "))
        L.removeAnywhere(index)
        print(f"Removed Item at index {index}!\n\n")
    elif choice == 7:
        print("List: ", end='')
        L.display()
        print("\n")

    elif choice == 8:
        print("Size:", len(L))
        print("\n")

    elif choice == 9:
        key = int(input("Enter item to search: "))
        if L.search(key) >= 0:
            print(f"Item {key} found at index position {L.search(key)}\n\n")
        else:
            print("Item not in the list\n\n")

    elif choice == 10:
        import sys
        sys.exit()


L = LinkedList()
while True:
    choice = options()
    switch_case(choice)
