from LinkedList.linkedlist import LinkedList
import sys
sys.path.append(".")


class HashChain:
    '''
    Initialises hashtable size and hashtable with respective head nodes using LinkedList() class.
    '''

    def __init__(self, hashsize=10) -> None:
        self._hashsize = hashsize
        self._hashtable = [0] * self._hashsize
        for i in range(self._hashsize):
            self._hashtable[i] = LinkedList()

    def hashcode(self, key):
        '''
        Returns Hash value using simple Mod operator.
        '''
        return key % self._hashsize

    def insert(self, element):
        '''
        Inserts element in hashtable.
        '''
        index = self.hashcode(element)
        self._hashtable[index].addSorted(element)

    def search(self, key):
        '''
        Returns index position if the element is found in the table, else False.
        '''
        position = self.hashcode(key)
        return self._hashtable[position].search(key)

    def display(self):
        '''
        Utility funtion to display Hashtable.
        '''
        for i in range(self._hashsize):
            print(f'[{i}] -- ', end='')
            self._hashtable[i].display()
        print()


###############################################################################


def options():
    '''
    Prints Menu for operations
    '''
    options_list = ['Insert Item', 'Search', 'Display Hashtable', 'Exit']

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
        H.insert(elem)
        print("Added Item.\n\n")

    elif choice == 2:
        elem = int(input("Enter Item to search: "))
        result = H.search(elem)
        if result != -1:
            print(f'Found Element at {result}.')
        else:
            print('Item does not exist.')

    elif choice == 3:
        print('HASHTABLE')
        H.display()

    elif choice == 4:
        import sys
        sys.exit()

###############################################################################


if __name__ == '__main__':
    H = HashChain(hashsize=10)
    while True:
        choice = options()
        switch_case(choice)
