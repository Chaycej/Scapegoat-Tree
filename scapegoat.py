import sys
import os
import math
import random
 
class Queue():
	def __init__(self):
		self.a = []
 
	def add(self, b):
		self.a.insert(0, b)
 
	def poll(self):
		return self.a.pop()
 
	def is_empty(self):
		return self.a == []
 
	def size(self):
		return len(self.a)


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

    def print_tree(self):
        lst = []
        self.inorder(lst, self.root)
        print(lst)

    def alpha_log(self, size):
        return math.log(size, 1/self.alpha)

    # Builds a list of nodes in sorted order
    def inorder(self, lst, root):
        if root is None:
            return
        self.inorder(lst[:], root.left)
        print("Inserting", root.val, "into list")
        lst.append(root)
        self.inorder(lst[:], root.right)

    # Returns the number of nodes in a sub-tree
    def size(self, node):
        if node is None:
            return 0
        return self.size(node.left) + self.size(node.right) + 1

    # Builds a tree from a sorted list of Nodes
    def build_tree(self, arr):
        if len(arr) <= 1:
            return arr[0]
        
        mid = int(len(arr)/2)
        arr[mid].left = self.build_tree(arr[:mid])
        if arr[mid].left != None:
            arr[mid].left.parent = arr[mid]
        arr[mid].right = self.build_tree(arr[mid:])
        if arr[mid].right != None:
            arr[mid].right.parent = arr[mid]
        return arr[mid]

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            self.tree_size += 1
        else:

            depth = 0
            current = self.root
            prev = None
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
                while ancestor.parent is not None:
                    alpha_size = self.size(ancestor) * self.alpha
                    if self.size(ancestor.left) <= alpha_size and self.size(ancestor.right) <= alpha_size:
                        ancestor = ancestor.parent
                    else:
                        scapegoat = ancestor
                        ancestor = ancestor.parent
                
                # Found top-level scapegoat node
                print("Scapegoat is", scapegoat.val)
                node_list = []
                self.inorder(node_list, scapegoat)
                print("Node list size is", len(node_list))
                for n in node_list:
                    print("Node in list is", n.val)
                sg_parent = scapegoat.parent


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
        print("size is", tree.tree_size)

    print_tree(tree.root, 1)

if __name__ == '__main__':
    main()
