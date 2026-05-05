#Building tree and binary tree from scratch
#Learning Reference - https://www.youtube.com/watch?v=EPwWrs8OtfI

"""
Trees have parents and children. Each parent can have atmost 2 children and a node can have atmost 1 parent.
If a tree has all the nodes in all levels filled out expect for the last level it's called a Completed Tree. If even the last level is filled out, it's called a perfect tree.
Binary tree's are never allowed to form cycles

There are two traversal methods:
- Depth First Search: We go deep with this search and there are two ways we can implement this algorithm: recursive and iterative
    - Sub Category of DFS:
        - Pre-Order: Process priority: node -> node.left -> node.right 
        - In-Order: Process priority: node.left -> node -> node.right
        - Post-Order: Process priority: node.left -> node.right -> node
    - To implement the iterative way we have to use a Stack and it's going to be pre-order traversal.

    Time Complexity: O(n)
    Space Complexity: O(n)

- Breadth First Search: We go wide with this search approach
    - We have to use a queue to implement this

Insert and Delete with BST:
"""