from singly_linked_list import SinglyNode
import unittest

class Test_SinglyLinkedListNode(unittest.TestCase):

    def setUp(self):
        self.Head = SinglyNode(10)
        A = SinglyNode(20)
        B = SinglyNode(30)
        C = SinglyNode(40)
    
        self.Head.next = A
        A.next = B
        B.next = C

    def test_node_initialization(self):
        self.assertEqual(self.Head.val, 10)
        self.assertEqual(self.Head.next.val, 20)
        self.assertEqual(self.Head.next.next.val, 30)
        self.assertEqual(self.Head.next.next.next.val, 40)

    def test_node_linking(self):
        self.assertEqual(self.Head.next.val, 20)
        self.assertEqual(self.Head.next.next.next.next, None)

    def test_node_traversing(self):
        output = []
        curr = self.Head
        while curr:
            output.append(curr.val)
            curr = curr.next

        self.assertEqual(output, [10, 20, 30, 40])

    def test_display_method(self):
        self.assertEqual(SinglyNode.display(head=self.Head), '10 -> 20 -> 30 -> 40')

    def test_search_node(self):
        self.assertEqual(SinglyNode.search(head=self.Head, val=10), 10)
    
    def test_add_to_end(self):
        D = SinglyNode(50)
        self.assertEqual(SinglyNode.add_to_end(head=self.Head, node=D), '10 -> 20 -> 30 -> 40 -> 50')

    def test_add_to_front(self):
        E = SinglyNode(60)
        self.assertEqual(SinglyNode.add_to_front(head=self.Head, node=E), '60 -> 10 -> 20 -> 30 -> 40')
    
    def test_add_to_middle(self):
        F = SinglyNode(70)
        self.assertEqual(SinglyNode.add_to_middle(head=self.Head, node=F, position=2), '10 -> 20 -> 30 -> 70 -> 40')

    def test_delete_from_beginning(self):
        self.assertEqual(SinglyNode.delete_from_beginning(head=self.Head), '20 -> 30 -> 40')

    def test_delete_from_end(self):
        self.assertEqual(SinglyNode.delete_from_end(head=self.Head), '10 -> 20 -> 30')
    
    def test_delete_by_value_middle(self):
        self.assertEqual(SinglyNode.delete_by_value(head=self.Head, val=30), '10 -> 20 -> 40')

    def test_delete_by_value_head(self):
        self.assertEqual(SinglyNode.delete_by_value(head=self.Head, val=10), '20 -> 30 -> 40')

    def test_delete_by_value_tail(self):
        self.assertEqual(SinglyNode.delete_by_value(head=self.Head, val=40), '10 -> 20 -> 30')

    def test_delete_by_value_not_found(self):
        self.assertEqual(SinglyNode.delete_by_value(head=self.Head, val=99), 'value not found')

    def test_delete_by_value_single_node(self):
        single = SinglyNode(10)
        self.assertEqual(SinglyNode.delete_by_value(head=single, val=10), '')
    
