#class for a Linked-list node
#Each node consists of a value and a pointer/reference to the next node. 
# Node A -> Node B (the arrow is the pointer in Node A)

class SinglyNode():

    #constructor
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    #dunder repr for debugging 
    def __repr__(self):
        return str(self.val)
    
    #display linked-list
    #time complexity: O(n)
    def display(head):
        output = []
        curr = head
        while curr:
            output.append(str(curr.val))
            curr = curr.next
        return " -> ".join(output)

    #search for node val
    #time complexity: O(n)
    def search(head, val):
        curr = head
        while curr:
            if curr.val == val:
                return curr.val
            curr = curr.next
        return f"{val} not found in linked list"
    
    #add a node to end of the linked list
    #time complexity: O(n)
    def add_to_end(head, node):
        if not head:
            head = node
            return
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = node
        return SinglyNode.display(head=head)
    
    #add a node to front of the linked list
    #time complexity: O(1)
    def add_to_front(head, node):

        node.next = head
        head = node
        
        return SinglyNode.display(head=head)

    #add a node in the middle of the linked list
    #time complexity: O(n)
    def add_to_middle(head, node, position):

        curr = head
        curr_position = 0

        while curr:

            if position == curr_position:
                temp = curr.next
                curr.next = node
                node.next = temp

            curr_position += 1
            curr = curr.next

        return SinglyNode.display(head=head)
    
    #Deletion Methods
    #time complexity: O(n)
    def delete_from_beginning(head):
        
        temp = head.next
        head.next = None
        head = temp

        return SinglyNode.display(head=head)

    #time complexity: O(n)
    def delete_from_end(head):

        if head.next == None:
            return None
        
        curr = head
        while curr.next.next:
            curr = curr.next
        curr.next = None

        return SinglyNode.display(head=head)

    #time complexity: O(n)
    def delete_by_value(head, val):

        if not head:
            return "Linked list is empty"

        if val == head.val:
            temp = head.next
            head.next = None
            head = temp
            return SinglyNode.display(head=head)

        curr = head

        while curr:

            if curr.next != None and val == curr.next.val:
                temp = curr.next
                curr.next = curr.next.next
                temp.next = None
                break
            
            curr = curr.next
        
        else:
            return "value not found"
        
        return SinglyNode.display(head=head)
        

        
        
        




        
        
