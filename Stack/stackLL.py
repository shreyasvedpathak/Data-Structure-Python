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


class StackLL:
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
        Returns length of stack.
        '''
        return self._size

    def isempty(self):
        '''
        Returns True if stack is empty, otherwise False.
        '''
        return self._size == 0

    def push(self, e):
        '''
        Pushes the passed element at the beginning of the linked list.
        That means, on the top of our stack.
        '''
        newest = _Node(e, None)

        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            newest._link = self._head
            self._head = newest
        self._size += 1

    def pop(self):
        '''
        Removes element from the beginning of the linked list.
        That means, pops element that is on the top.
        Returns the removed element.
        '''
        if self.isempty():
            print("Stack is Empty. Cannot perform Pop operation.")
            return

        e = self._head._element
        self._head = self._head._link
        self._size = self._size - 1

        if self.isempty():
            self._tail = None

        return e
    
    def top(self):
        '''
        Peeks at the element on the top of the stack.
        '''
        if self.isempty():
            print("Stack is Empty. Cannot perform Pop operation.")
            return

        e = self._head._element
        return e

    def display(self):
        '''
        Utility function to display the Stack.
        '''
        if self.isempty() == 0:
            p = self._head
            while p:
                print(p._element)
                p = p._link
        else:
            print("Empty")

###############################################################################

def options():
    '''
    Prints Menu for operations
    '''
    options_list = ['Push', 'Pop', 'Top',
                    'Display Stack', 'Exit']

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
        S.push(elem)

    elif choice == 2:
        print('Popped item is: ', S.pop())

    elif choice == 3:
        print("Item on top is: ", S.top())

    elif choice == 4:
        print("Stack:")
        S.display()
        print("\n")

    elif choice == 5:
        import sys
        sys.exit()

###############################################################################

if __name__ == '__main__':
    S = StackLL()
    while True:
        choice = options()
        switch_case(choice)