#Implementation of a Heap/Priority Queue data structure from scratch

"""
A heap or priority queue are the same data structure and can be used interchangeably.  

Heap can be implemented using a dynamic array. There are generally two types of heaps - min heap and max heap. 

There are two properties a min or max heap should satisfy:
    1. Structure property: It should be a complete tree. i.e only the end nodes can have empty values 
    2. Order property: Parent should be always smaller than the children nodes (for max heap it's the inverse)

Example:

A = [0,-4,1,2,3,4,5,6,7,8,9,10] will be represented like: (always make sure the actual values are 1 indexed. So the 0th element is always a dummy node)

                    -4          (index 1)
                 /      \
               1          2     (index 2, 3)
             /   \       /  \
            3     4     5    6  (index 4, 5, 6, 7)
           / \   / \   / \
          7   8 9  10          (index 8, 9, 10, 11)

          
Given index i the formulae to get
- left node: 2i
- right node: 2i + 1
- parent: i // 2

Ex: Given index 4 (value 4)
- left node: 2(4). 8th index value is 7 which is indeed the left child node of 3.
- right node: 2(4) + 1 = 9. 8th index value is 8 which is indeed the right child node of 3.
- parent = 4 // 2 = 2. 2nd index value is 1 which is it's parent. 
        
"""

class Heap:

    def __init__(self):
        self.heap = [0] 
    
    def push(self, val):

        self.heap.append(val)
        i = len(self.heap) - 1

        #percolate up
        while i > 1 and self.heap[i] < self.heap[i//2]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i // 2
    
    def __repr__(self):
        return str(self.heap)





















#testing

A = Heap()

A.push(-4)
A.push(1)
A.push(2)
A.push(3)
A.push(4)
A.push(6)
A.push(7)
A.push(8)
A.push(9)
A.push(10)
A.push(-1)


print(A)