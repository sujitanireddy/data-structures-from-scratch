#Building Binary tree from scratch
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
"""

import collections


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)

    #Depth first search
    #Recursive Pre-order/In-order/Post-order traversals
    # TC: O(n) SC: O(n)
    def recursive_preorder(node):

        if not node:
            return
    
        print(node)
        TreeNode.recursive_preorder(node.left)
        TreeNode.recursive_preorder(node.right)
    
    def recursive_inorder(node):

        if not node:
            return
    
        TreeNode.recursive_inorder(node.left)
        print(node)
        TreeNode.recursive_inorder(node.right)

    def recursive_postorder(node):

        if not node:
            return
    
        TreeNode.recursive_postorder(node.left)
        TreeNode.recursive_postorder(node.right)
        print(node)

    #Iterative Pre-order traversal
    #TC: O(n) SC: O(n)
    def iterative_preorder(node):
        stk = [node]
        while stk:
            node = stk.pop()
            print(node)
            if node.right: stk.append(node.right)
            if node.left: stk.append(node.left)

    #Breadth first search
    #TC: O(n) SC: O(n)
    def iterative_BFS(node):
        q = collections.deque()
        q.append(node)

        while q:
            node = q.popleft()
            print(node)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

    #Search function
    #TC: O(n) SC: O(n)
    def search(node, target):

        if not node:
            return False

        if node.val == target:
            return True
        
        return TreeNode.search(node.left, target) or TreeNode.search(node.right, target)
















#Testing
A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

#        1
#     2    3
#   4  5  10

#print(A)

#TreeNode.recursive_preorder(A)
#TreeNode.recursive_inorder(A)
#TreeNode.recursive_postorder(A)
#TreeNode.iterative_preorder(A)
#TreeNode.iterative_BFS(A)
print(TreeNode.search(A, 5))
        

