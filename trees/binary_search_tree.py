#Building Binary Search Tree from Scratch

from binary_tree import TreeNode

#TC: O(logn)
def search_bst(node, target):    
    if not node:
        return False

    if node.val == target:
        return True
    if node.val > target: 
        return search_bst(node.left, target)
    else:
        return search_bst(node.right, target)

#TC: O(logn)
def insert(root ,val):
    if not root:
        return TreeNode(val)

    if root.val < val:
        root.right = insert(root.right, val)
    elif root.val > val:
        root.left = insert(root.left, val)
    return root

#Find min 
def find_min(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

#Removing a node for a BST
#TC: O(logn)
def remove(root, val):
    if not root:
        return None
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.right:
            return root.left
        elif not root.left:
            return root.right
        else:
            min_node = find_min(root.right)
            root.val = min_node.val
            root.right = remove(root.right, min_node.val)
    return root



#testing 
# Binary Search Trees (BSTs)

#       5
#    1    8
#  -1 3  7 9

A2 = TreeNode(5)
B2 = TreeNode(1)
C2 = TreeNode(8)
D2 = TreeNode(-1)
E2 = TreeNode(3)
F2 = TreeNode(7)
G2 = TreeNode(9)

A2.left, A2.right = B2, C2
B2.left, B2.right = D2, E2
C2.left, C2.right = F2, G2

#print(A2)
#TreeNode.recursive_inorder(A2)
#print(search_bst(A2, 100))
print(insert(A2, 14))