import sys
import os
import random




class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



class Tree:

    def __init__(self):
        self.size = 0;
        self.root = None


    def get_size(self):
        return self.size


    def print_tree(self):
        lst = []
        self.inorder(lst, self.root)
        print(lst)


    def inorder(self, lst, root):
        if root is None:
            return
        self.inorder(lst, root.left)
        lst.append(root.val)
        self.inorder(lst, root.right)


    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            self.size += 1
        else:

            current = self.root
            prev = None
            while current != None:
                if current.val > val:
                    prev = current
                    current = current.left
                else:
                    prev = current
                    current = current.right

            if prev.val > val:
                prev.left = Node(val)
            else:
                prev.right = Node(val)
            self.size += 1



    def search(self, val):
        if self.root is None:
            return false
        else:

            current = self.root
            while current != None:
                if current.val > val:
                    current = current.left
                elif current.val < val:
                    current = current.right
                else:
                    return True
            return False


def main():
    tree = Tree()

    for i in range(10000):
        tree.insert(random.randint(1, 10000))

    tree.print_tree()
    print(tree.get_size())

if __name__ == '__main__':
    main()
