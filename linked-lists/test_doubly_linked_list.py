import unittest
from doubly_linked_list import doublyNode

class Test_DoublyLinkedListNode(unittest.TestCase):

    def setUp(self):
        self.Head = self.Tail = doublyNode(10)
        A = doublyNode(20)
        B = doublyNode(30)
        C = doublyNode(40)
    
        self.Head.next = A
        self.Head.prev = None
        A.next = B
        A.prev = self.Head
        B.next = C
        B.prev = A
        C.prev = B
        self.Tail = C
    
    def test_display_method(self):
        self.assertEqual(doublyNode.display(head=self.Head, tail=None), '10 <-> 20 <-> 30 <-> 40')
        self.assertEqual(doublyNode.display(tail=self.Tail, head=None), '40 <-> 30 <-> 20 <-> 10')
        self.assertEqual(doublyNode.display(tail=self.Tail, head=self.Head), '10 <-> 20 <-> 30 <-> 40')


