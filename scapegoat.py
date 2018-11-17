import sys
import os
import math
import random

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Tree:

    def __init__(self, alpha):
        self.root = None
        self.tree_size = 0
        self.alpha = alpha

    # Prints a tree using inorder traversal
    def print_tree(self):
        lst = []
        self.inorder(lst, self.root)
        print(lst)

    # Equation used to check if a rebuild is triggered (depth > alpha_Log(tree_size))
    def alpha_log(self, size):
        return math.log(size, 1/self.alpha)

    # Builds a list of nodes in sorted order
    def inorder(self, lst, root):
        if root is None:
            return
        self.inorder(lst, root.left)
        lst.append(root)
        self.inorder(lst, root.right)

    # Returns the number of nodes in a sub-tree
    def size(self, node):
        if node is None:
            return 0
        return self.size(node.left) + self.size(node.right) + 1

    # Builds a binary search tree from a sorted list of Nodes
    def build_tree(self, arr):
        if not arr:
            return None
        
        mid = int(len(arr)/2)
        root = arr[mid]
        root.left = self.build_tree(arr[:mid])
        if root.left != None:
            root.left.parent = root
        root.right = self.build_tree(arr[mid+1:])
        if root.right != None:
            root.right.parent = root
        return root

    # Inserts an element into the tree. If the inserted node is too deep,
    # a rebuild is triggered by finding the top-level node that has uneven left
    # and right braches and rebuilding the tree.
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            self.tree_size += 1
        else:

            depth = 0
            current = self.root
            prev = None

            # Find position to insert new node
            while current != None:
                prev = current
                if current.val > val:
                    current = current.left
                else:
                    current = current.right
                depth += 1

            if prev.val > val:
                prev.left = Node(val)
                prev.left.parent = prev
            else:
                prev.right = Node(val)
                prev.right.parent = prev

            self.tree_size += 1

            # Node is too deep, rebuild tree
            if depth > math.floor(self.alpha_log(self.tree_size) + 1):
                print("rebuild triggered after inserting", val)

                scapegoat = prev
                ancestor = prev

                # Find highest level scapegoat node
                while ancestor.parent is not None:
                    alpha_size = self.size(ancestor) * self.alpha
                    if self.size(ancestor.left) <= alpha_size and self.size(ancestor.right) <= alpha_size:
                        ancestor = ancestor.parent
                    else:
                        scapegoat = ancestor
                        ancestor = ancestor.parent
                
                # Found top-level scapegoat node, rebuild subtree
                sg_parent = scapegoat.parent
                node_list = []
                self.inorder(node_list, scapegoat)
                new_root = self.build_tree(node_list)
                
                if sg_parent.left == scapegoat:
                    new_root.parent = sg_parent
                    sg_parent.left = new_root
                else:
                    new_root.parent = sg_parent
                    sg_parent.right = new_root

    # Returns True if the value is found in the tree, False otherwise.
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

# Pretty print a tree
def print_tree(node, level):
    if node is not None:
        print_tree(node.left, level+4)
        print(" "*level, node.val)
        print_tree(node.right, level+4)

def BuildTree(alpha, key):
    t = Tree(alpha)
    t.insert(key)
    return t


def main():
    tree = Tree(0.57)
    for i in range(1, 10):
        num = random.randint(1, 30)
        print("Inserting", num)
        tree.insert(num)

    print_tree(tree.root, 1)

if __name__ == '__main__':
    main()
