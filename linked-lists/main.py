#class for a Linked-list node
#Each node consists of a value and a pointer/reference to the next node. 
# Node A -> Node B (the arrow is the pointer in Node A)

class Node():

    #constructor
    def __init__(self, val, next):
        self.val = val
        self.next = next
    
    #dunder repr for debugging 
    def __repr__(self):
        return f"[val = {self.val}, next = {self.next}] -> "

