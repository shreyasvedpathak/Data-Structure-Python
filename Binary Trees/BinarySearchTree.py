# Import the BinaryTree package from the same directory.
from BinaryTree import BinaryTree, _Node


class BST:
    def __init__(self):
        '''
        Initialises the root to None and creates instance of Binary Tree modules,
        from the BinaryTree.py file.
        '''
        self._root = None
        self.BT = BinaryTree()

    def insertion_iterative(self, e):
        '''
        Inserts an item into the BST using Iterative Approach
        '''
        temp = None
        troot = self._root
        while troot:
            temp = troot
            if e < troot._element:
                troot = troot._left
            else:
                troot = troot._right

        if self._root:
            if e < temp._element:
                temp._left = _Node(e)
            else:
                temp._right = _Node(e)
        else:
            self._root = _Node(e)

    def insertion_recursive(self, troot, e):
        '''
        Inserts an item into the BST using Recursive Approach
        '''
        if troot:
            if e < troot._element:
                troot._left = self.insertion_recursive(troot._left, e)
            elif e > troot._element:
                troot._right = self.insertion_recursive(troot._right, e)
        else:
            troot = _Node(e)
        return troot

    def search_iterative(self, key):
        '''
        Searches for an item in the BST using Iterative Approach
        '''
        troot = self._root
        while troot:
            if key == troot._element:
                return True
            elif key < troot._element:
                troot = troot._left
            elif key > troot._element:
                troot = troot._right
        return False

    def search_recursive(self, troot, key):
        '''
        Searches for an item in the BST using Recursive Approach
        '''
        if troot:
            if key == troot._element:
                return True
            elif key < troot._element:
                return self.search_recursive(troot._left, key)
            elif key > troot._element:
                return self.search_recursive(troot._right, key)
        else:
            return False

    def delete(self, key):
        '''
        Deletes an item in the BST

        p  -- reference to the node we want to delete
        pp -- reference to parent node of p
        s  -- reference to the largest element in the left subtree
        ps -- reference to the node we want to delete (temporary)
              later it becomes parent to s node
        c  -- reference to the child node
        '''
        p = self._root
        pp = None

        # Finding the Node we want to delete
        while p and p._element != key:
            pp = p
            if key < p._element:
                p = p._left
            else:
                p = p._right

        # If the Node doesn't exist in the tree.
        if not p:
            return False

        # If the Node has both left and right sub tree.
        if p._left and p._right:
            s = p._left
            ps = p
            # Finds the largest element in the left subtree
            while s._right:
                ps = s
                s = s._right
            p._element = s._element
            p = s
            pp = ps

        # If the node has atmost one child i.e. left child or right child
        # or no child (lead node)
        c = None
        if p._left:
            c = p._left
        else:
            c = p._right

        if p == self._root:
            self._root = None
        else:
            if p == pp._left:
                pp._left = c
            else:
                pp._right = c

        return True

    def inorder(self):
        self.BT.inorder(self._root)


def options():
    '''
    Prints Menu for operations
    '''
    options_list = ['Add an item (Iterative)', 'Add multiple items (Iterative)',
                    'Add an item (Recursive)', 'Add multiple items (Recursive)',
                    'Search (Iterative)', 'Search (Recursive)', 'Delete',
                    'Display BST (Inorder)', 'Exit']
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
        elem = int(input("Enter an item: "))
        bst.insertion_iterative(elem)

    elif choice == 2:
        A = list(map(int, input("Enter numbers: ").split()))
        for elem in A:
            bst.insertion_iterative(elem)

    elif choice == 3:
        elem = int(input("Enter an item: "))
        bst.insertion_recursive(elem)

    elif choice == 4:
        A = list(map(int, input("Enter numbers: ").split()))
        for elem in A:
            bst.insertion_recursive(elem)

    elif choice == 5:
        elem = int(input("Enter an item to search: "))
        print("Found item.") if bst.search_iterative(
            elem) else print("Item does not exist.")

    elif choice == 6:
        elem = int(input("Enter an item to search: "))
        print("Found item.") if bst.search_recursive(bst._root,
                                                     elem) else print("Item does not exist.")

    elif choice == 7:
        elem = int(input("Enter an item to delete: "))
        print("Item Deleted.") if bst.delete(
            elem) else print("Item doesn't exist.")

    elif choice == 8:
        print("Inorder Traversal:")
        bst.inorder()

    elif choice == 9:
        import sys
        sys.exit()

###############################################################################


if __name__ == '__main__':
    bst = BST()
    while True:
        choice = options()
        switch_case(choice)
