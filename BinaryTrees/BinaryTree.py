import sys
sys.path.append(".")
from Queue.queueLL import QueueLL

class _Node:
    '''
    Initialises node with the passed arguments, None if no arguments are passed.
    '''
    __slots__ = '_element', '_left', '_right'
    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right

class BinaryTree:
    def __init__(self):
        '''
        Initialises Root node to None.
        '''
        self._root = None
        self._count = 0

    def __len__(self):
        '''
        Returns the length of Tree.
        '''
        return self._count

    def createTree(self, node):
        '''
        Recursively adds node to the tree using Postorder traversing pattern.
        That means, it will first ask to add all the left childs of root
        and then right child of the most recently added node.
        '''
        # os.system('cls')
        position = input(
            f"Add node on the Left of {node._element} ? [y/n]: ")
        if position == 'y':
            nodeData = input("Enter data for node: ")
            curr = _Node(nodeData)
            node._left = curr
            self.createTree(curr)
            self._count += 1

        # os.system('cls')
        position = input(
            f"Add node on the Right of {node._element} ? [y/n]: ")
        if position == 'y':
            nodeData = input("Enter data for node: ")
            curr = _Node(nodeData)
            node._right = curr
            self.createTree(curr)
            self._count += 1

    def createRoot(self):
        '''
        Function to create Root node.
        '''
        rootData = input("Enter data for Root: ")
        self._root = _Node(rootData)
        self.createTree(self._root)
        self._count += 1

    def inorder(self, troot):
        '''
        Function for Inorder Traversal.
        '''
        if troot:
            self.inorder(troot._left)
            print(troot._element, end=" ")
            self.inorder(troot._right)

    def preorder(self, troot):
        '''
        Function for Preorder Traversal.
        '''
        if troot:
            print(troot._element, end=" ")
            self.preorder(troot._left)
            self.preorder(troot._right)

    def postorder(self, troot):
        '''
        Function for Postorder Traversal.
        '''
        if troot:
            self.postorder(troot._left)
            self.postorder(troot._right)
            print(troot._element, end=" ")

    def levelorder(self):
        Q = QueueLL()
        t = self._root
        print(t._element, end=" ")
        Q.enqueue(t)

        while not Q.isempty():
            t = Q.dequeue()
            if t._left:
                print(t._left._element, end=" ")
                Q.enqueue(t._left)
            if t._right:
                print(t._right._element, end=" ")
                Q.enqueue(t._right)

    def height(self, troot):
        '''
        Utility function to calculate height of the tree.
        '''
        if troot:
            x = self.height(troot._left)
            y = self.height(troot._right)

            if x > y:
                return x + 1
            else:
                return y + 1
            
        return 0

###############################################################################


def options():
    '''
    Prints Menu for operations
    '''
    options_list = ['Create Tree', 'Inorder', 'Preorder',
                    'Postorder', 'Level Order', 'Count',
                    'Height', 'Exit']

    print("\nMENU")
    for i, option in enumerate(options_list):
        print(f'{i + 1}. {option}')

    choice = int(input("Enter choice: "))
    return choice


def switch_case(choice):
    '''
    Switch Case for operations
    '''
    # os.system('cls')
    if choice == 1:
        bt.createRoot()

    elif choice == 2:
        print("Inorder Traversal:")
        bt.inorder(bt._root)

    elif choice == 3:
        print("Preorder Traversal:")
        bt.preorder(bt._root)

    elif choice == 4:
        print("Postorder Traversal:")
        bt.postorder(bt._root)
    elif choice == 5:
        print("Level Order Traversal:")
        bt.levelorder()
    elif choice == 6:
        print("Number of Nodes: ",len(bt))
    
    elif choice == 7:
        print("Height: ", bt.height(bt._root) - 1)

    elif choice == 8:
        sys.exit()

###############################################################################

if __name__ == '__main__':
    bt = BinaryTree()
    while True:
        choice = options()
        switch_case(choice)

'''
MENU
1. Create Tree
2. Inorder    
3. Preorder   
4. Postorder  
5. Exit       
Enter choice: 1
Enter data for Root: 10
Add node on the Left of 10 ? [y/n]: y
Enter data for node: 20
Add node on the Left of 20 ? [y/n]: n
Add node on the Right of 20 ? [y/n]: n
Add node on the Right of 10 ? [y/n]: y
Enter data for node: 30
Add node on the Left of 30 ? [y/n]: n
Add node on the Right of 30 ? [y/n]: n

MENU
1. Create Tree
2. Inorder
3. Preorder
4. Postorder
5. Exit
Enter choice: 2
Inorder Traversal:
20 10 30
MENU
1. Create Tree
2. Inorder
3. Preorder
4. Postorder
5. Exit
Enter choice: 3
Preorder Traversal:
10 20 30
MENU
1. Create Tree
2. Inorder
3. Preorder
4. Postorder
5. Exit
Enter choice: 4
Postorder Traversal:
20 30 10
'''