#Doubly linked lists class
#Each doubly linked list node consists of reference to the next node and the previous node. 
# A <-> B <-> C

class doublyNode():

    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
    
    def __repr__(self):
        return str(self.val)
    
    def display(head, tail):

        linked_list = []

        #traversing the list from the end if tail is provided
        if tail and not head:
            curr = tail
            while curr:
                linked_list.append(str(curr.val))
                curr = curr.prev
            return ' <-> '.join(linked_list)

        else:
            curr = head
            while curr:
                linked_list.append(str(curr.val))
                curr = curr.next
            return ' <-> '.join(linked_list)

        

        
