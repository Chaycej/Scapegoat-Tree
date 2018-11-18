Chayce Heiberg
Chayce.heiberg@wsu.edu

This is an implementation of a scapegoat tree written in python 3. The program requires a file
called "tree.txt" that has 1 command per line. A command can be "BuildTree <float> <int>", 
"Insert <int>", "Delete <int>", "Print", or "Done".

BuildTree:
    Creates a scapegoat tree with a specified alpha value (float), and an initial value to insert (int).

Insert:
    Inserts a value (int) into the tree. If a subtree needs rebuilt, a rebuilding message will be displayed

Delete:
    Deletes a value (int) from the tree. If the tree needs rebuilt, a rebuilding message will be displayed.

Print:
    Prints the tree in using an inorder traversal. The tree is on its side and its branches are mirrored.

    Example:
                    7
            8
    10
            11
                    12
    
        represents                  10
                                8       11
                              7             12


To run the program:
    execute "python3 scapegoat.py" in the terminal
    Make sure there is a file named "tree.txt" with commands, in order for the program to build the tree

File archive:
    scapegoat.py - Scapegoat source code
    README.md   - readme file explaining the program
    tree.txt - example input file
