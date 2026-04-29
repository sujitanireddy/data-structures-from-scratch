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

    def pop(self):

        if len(self.heap) == 1:
            return None

        if len(self.heap) == 2:
            return self.heap.pop()

        minn = self.heap[1]
       
        #move last node to root
        self.heap[1] = self.heap.pop()

        i = 1

        while 2 * i < len(self.heap): #while left child exists

            #(2 * i) + 1 = right node, 2*i = left node
            #if right node exists and it's less than left node and parent is less than right node then swap right
            if (2 * i) + 1 < len(self.heap) and self.heap[(2 * i) + 1] < self.heap[(2*i)] and self.heap[i] > self.heap[(2 * i) + 1]:

                self.heap[(2 * i) + 1], self.heap[i] = self.heap[i], self.heap[(2 * i) + 1]

                i = (2 * i) + 1
            
            elif self.heap[i] > self.heap[2 * i]:

                self.heap[2 * i], self.heap[i] = self.heap[i], self.heap[2 * i]

                i = 2 * i
            
            else:
                break
    
        return minn



    
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
A.pop()

print(A)