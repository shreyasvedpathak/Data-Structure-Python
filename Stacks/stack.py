import os

class Stacks:
    def __init__(self):
        '''
        Initialises a empty list which will be used as Stack array.
        '''
        self._data = []
    
    def __len__(self):
        '''
        Returns length of Stack>
        '''
        return len(self._data)
    
    def isempty(self):
        '''
        Returns True if stack is empty, else False.
        '''
        return len(self._data) == 0

    def push(self, e):
        '''
        Pushes the passed element(e) on the stack.
        '''
        self._data.append(e)
    
    def pop(self):
        '''
        Removes the element on the top and returns it.
        '''
        if self.isempty():
            print("Stack is Empty")
            return
        
        return self._data.pop()

    def top(self):
        '''
        Peeks at the element on the top of the stack.
        '''
        if self.isempty():
            print("Stack is Empty")
            return

        return self._data[-1]
    
    def display(self):
        '''
        Utility function to display the stack.
        '''
        if self.isempty():
           print("Stack is Empty")
           return
        print("Stack:")
        for item in reversed(self._data):
            print(item)

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
        print("Stack: ", end='')
        S.display()
        print("\n")

    elif choice == 5:
        import sys
        sys.exit()

###############################################################################

S = Stacks()
while True:
    choice = options()
    switch_case(choice)
