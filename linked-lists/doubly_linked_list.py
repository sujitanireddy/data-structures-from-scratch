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
        
    
    #Time Complexity: O(1)
    def add_to_beginning(node, head, tail):

        if head is None:
            return "No head to attach the node"

        head.prev = node
        node.next = head
        node.prev = None
        head = node

        return doublyNode.display(head=head, tail=None)
    
    #Time Complexity: O(1); if tail is provided if not it's O(n)
    def add_to_end(node, head, tail):
        
        if head and not tail:
            curr = head
            while curr:
                tail = curr
                curr = curr.next
            
            tail.next = node
            node.next = None
            node.prev = tail
            tail = node
        
        if tail:

            tail.next = node
            node.next = None
            node.prev = tail
            tail = node

        return doublyNode.display(head=head, tail=tail)



