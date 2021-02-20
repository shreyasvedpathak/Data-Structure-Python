import os


class HashLP:
    def randomPrime(self, upper):
        '''
        Generates a random prime number for hash_2 function.
        '''
        import random
        
        prime = []
        for num in range(upper + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    prime.append(num)
        
        return random.choice(prime)

    def __init__(self, hashsize=10) -> None:
        '''
        Initialises hashtable size and prime number.
        '''
        self._hashsize = hashsize
        self._hashtable = [-1] * self._hashsize
        self._size = 0
        self._q = self.randomPrime(self._hashsize)
        print(f'[ NOTE: Prime Number chosen: {self._q} ]')

    def isfull(self):
        '''
        Returns True if Hash table is full, otherwise False.
        '''
        return self._size == self._hashsize

    def isempty(self):
        '''
        Returns True if Hash table is empty, otherwise False.
        '''
        return self._size == 0

    def hash_1(self, key):
        '''
        Returns Hash value using simple Mod operator.
        '''
        return key % self._hashsize

    def hash_2(self, key):
        '''
        Returns Hash value using prime number.
        '''
        return self._q - (key % self._q)

    def findnext(self, index_h1, index_h2, method='linear', factor=1):
        '''
        This function is used to calculate the next index position based on
        following parameters if the collision occurs.

        {parameters} :  'index_h1' -- Hash value by hash_1 function
                        'index_h2' -- Hash value by hash_2 function
                        'linear'  -- Linear Probing
                        'quad'   -- Quadratic Probing
                        'double' -- Double Hashing

        {returns} : Returns index when collison occurs.
        '''

        if method == 'linear':
            return (index_h1 + factor) % self._hashsize
        elif method == 'quad':
            return (index_h1 + factor ** 2) % self._hashsize
        elif method == 'double':
            return (index_h1 + (factor * index_h2)) % self._hashsize

    def insert(self, element, method='linear'):
        '''
        Inserts element in hashtable using the passed Method.
        '''
        if self.isfull():
            print('Hash Table is Full !')
            return False

        position = index_h1 = self.hash_1(element)
        index_h2 = self.hash_2(element)

        n = 0
        while self._hashtable[position] != -1:
            n += 1
            position = self.findnext(
                index_h1, index_h2, method=method, factor=n)

        self._hashtable[position] = element
        self._size += 1
        return True

    def search(self, key, method='linear'):
        '''
        Returns index position if the element is found in the table, else False.
        '''
        if self.isempty():
            print('Hashtable is empty')
        else:
            position = index_h1 = self.hash_1(key)
            index_h2 = self.hash_2(key)
            n = 0
            while True:
                if self._hashtable[position] == key:
                    return position
                else:
                    n += 1
                    position = self.findnext(
                        index_h1, index_h2, method=method, factor=n)
                    if position == index_h1 - 1:
                        break
            return

    def display(self):
        '''
        Utility funtion to display Hashtable.
        '''
        if self.isempty():
            print('Hashtable is empty')
        else:
            for i, element in enumerate(self._hashtable):
                print(f'[{i}] -- {element}')

###############################################################################


def method():
    '''
    Prints different methods for selecting a Hashing strategy.
    '''
    methods = ['Linear Probing', 'Quadratic Probing', 'Double Hashing']
    method_arg = ['linear', 'quad', 'double']

    print("Chose a Method for collision case:")
    for i, method in enumerate(methods):
        print(f'{i + 1}. {method}')

    method = int(input("Enter choice: "))
    method = method_arg[method - 1]

    return method


def options(method):
    '''
    Prints Menu for operations
    '''
    options_list = ['Insert Item', 'Search', 'Display Hashtable', 'Exit']

    print(f"MENU for Hash Table using '{method}' strategy.")
    for i, option in enumerate(options_list):
        print(f'{i + 1}. {option}')

    choice = int(input("Enter choice: "))
    return method, choice


def switch_case(method, choice):
    '''
    Switch Case for operations
    '''
    if choice == 1:
        elem = int(input("Enter item: "))
        print("Added item.") if H.insert(
            elem, method=method) else print('Item cannot be added.')

    elif choice == 2:
        elem = int(input("Enter item to search: "))
        result = H.search(elem, method=method)
        print(f'Found element at {result}.') if result != None else print(
            'Item does not exist.')

    elif choice == 3:
        print('HASHTABLE')
        H.display()

    elif choice == 4:
        import sys
        sys.exit()

###############################################################################


if __name__ == '__main__':
    n = int(input('Enter hash table size: '))
    H = HashLP(hashsize=n)
    method = method()
    os.system('cls')
    while True:
        method, choice = options(method)
        switch_case(method, choice)
