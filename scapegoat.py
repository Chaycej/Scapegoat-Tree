import sys
import os
import math
import random

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:

    def __init__(self, alpha):
        self.root = None
        self.tree_size = 0
        self.max_node_count = 0;
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

            parent_list = []

            # Find position to insert new node
            while current != None:
                parent_list.append(current)
                prev = current
                if current.val > val:
                    current = current.left
                else:
                    current = current.right
                depth += 1

            if prev.val > val:
                prev.left = Node(val)
            else:
                prev.right = Node(val)

            self.tree_size += 1
            self.max_node_count = max(self.tree_size, self.max_node_count)

            # Node is too deep, rebuild tree
            if depth > math.floor(self.alpha_log(self.tree_size) + 1):
                print("rebuild triggered after inserting", val)

                scapegoat = None
                scapegoat_index = 0
                
                # Find highest level scapegoat node
                for i in range(1, len(parent_list)):
                    ancestor = parent_list[i]
                    alpha_size = self.size(ancestor) * self.alpha
                    if self.size(ancestor.left) <= alpha_size and self.size(ancestor.right) <= alpha_size:
                        continue
                    else:
                        scapegoat = ancestor
                        scapegoat_index = i
                        break
                
                # Found top-level scapegoat node, rebuild subtree
                print("Scapegoat is", scapegoat.val)
                sg_parent = parent_list[scapegoat_index-1]
                node_list = []
                self.inorder(node_list, scapegoat)
                new_root = self.build_tree(node_list)
                
                if sg_parent.left == scapegoat:
                    sg_parent.left = new_root
                else:
                    sg_parent.right = new_root


    # Returns the minimum node in a subtree
    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


    # Deletes a node in the tree and rebuilds the entire tree if the
    # updated size is less than or equal to the max size times alpha.
    def delete(self, val):
        self.delete_node(val, self.root)
        self.tree_size -= 1


    # Auxiliary function for delete()
    def delete_node(self, val, node):
        if node is None:
            return None
        
        if node.val < val:
            node.right = self.delete_node(val, node.right)
        elif node.val > val:
            node.left = self.delete_node(val, node.left)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Replace node to be deleted with successor node 
            temp = self.find_min(node.right)
            print("min is", temp.val)
            node.val = temp.val
            node.right = self.delete_node(temp.val, node.right)

        # Delete triggered rebuild of entire tree
        if self.tree_size <= self.alpha * self.max_node_count:
            print("Delete triggered rebuild of entire tree")
            node_list = []
            self.inorder(node_list, self.root)
            self.root = self.build_tree(node_list)
            return self.root
        else:
            return node


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

    
def main():
    
    try:
        file = open("tree.txt", mode="r")
    except:
        print("File must be named 'tree.txt'")
        sys.exit(1)

    cmd_list = [line.rstrip("\n").replace(",", "") for line in file]
    t = None

    for cmd in cmd_list:
        cmd = cmd.split()

        if cmd[0] == "BuildTree":
            if t is not None:
                print("Already built tree! Ignoring this command")
                continue
            print("Building tree")
            t = Tree(float(cmd[1]))
            t.insert(int(cmd[2]))
        elif cmd[0] == "Insert":
            print("Inserting", cmd[1])
            t.insert(int(cmd[1]))
        elif cmd[0] == "Delete":
            print("Deleting", cmd[1])
            t.delete(int(cmd[1]))
        elif cmd[0] == "Print":
            print("Printing tree")
            print_tree(t.root, 1)
        elif cmd[0] == "Done":
            print("Exiting program")
            sys.exit(0)
        else:
            print("Unrecognized command, exiting program")
            sys.exit(1)

if __name__ == '__main__':
    main()
