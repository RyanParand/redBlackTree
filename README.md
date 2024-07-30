# redBlackTree
Ryan Parand
I used pythone3 to implement red black tree algorithm.

refrences:
    1. professor Nick Painter's lecture notes (CSE2331 - Spring 2024)
    2. ChatGPT

A red-black tree is a binary search tree with the following properties:
    1. Every node is either red or black.
    2. The root is black.
    3. Every leaf is NIL and is black.
    4. If a node is red, then both its children are black.
    5. For each node, all simple paths from the node to descendant leaves contain the same number of black nodes.

Methods:
    insert(value): Insert a new value while maintaining tree properties.
    delete(value): Remove a value while maintaining tree properties.
    search(value): Search for a value in the tree.
    traverse(order): Traverse the tree (in-order, pre-order, post-order).

Scenarios:
    Random input sequences.
    Sorted input sequences.
    Reverse sorted input sequences.

Visualization:
    Graphics library, Graphviz or a GUI framework like Qt.

Please run this program in linux system or wsl
please make sure you have pythone 3 installed
please make sure you have python3-pip is installed:  sudo apt install python3-pip
please make sure pip install networkx matplotlib
