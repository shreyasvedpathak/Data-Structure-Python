import os


class Queue:
    def __init__(self):
        self._data = []

    def __len__(self):
        '''
        Returns length of Queue
        '''
        return len(self._data)

    def isempty(self):
        '''
        Returns True if Queue is empty, otherwise False.
        '''
        return self.__len__ == 0

    def enqueue(self, e):
        '''
        Adds the passed element at the end of the list.
        That means, it enqueues element.
        '''
        self._data.append(e)

    def dequeue(self):
        '''
        Removes element from the beginning of the list and 
        returns the removed element.
        That means, it dequeues.
        '''
        if self.isempty():
            print("Queue is empty.")
            return

        return self._data.pop(0)

    def first(self):
        '''
        Peeks and return the first element in the Queue.
        '''
        if self.isempty():
            print("Queue is empty.")
            return

        return self._data[0]

    def display(self):
        '''
        Utility function to display the Queue.
        '''
        if self.isempty():
            print("Queue is empty.")
        else:
            print("Front", end=' <--')
            for i in self._data:
                print(i, end='<--')
            print(" Rear")

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
    Q = Queue()
    while True:
        choice = options()
        switch_case(choice)
