#Tests for Singly LinkedList
from main import SinglyNode
import unittest

class Test_SinglyLinkedListNode(unittest.TestCase):

    def test_node_initialization(self):

        Head = SinglyNode(10)
        A = SinglyNode(20)
        B = SinglyNode(30)
        C = SinglyNode(40)

        self.assertEqual(Head.val, 10)
        self.assertEqual(A.val, 20)
        self.assertEqual(B.val, 30)
        self.assertEqual(C.val, 40)
    
    def test_node_linking(self):

        Head = SinglyNode(10)
        A = SinglyNode(20)
        B = SinglyNode(30)
        C = SinglyNode(40)

        Head.next = A
        A.next = B
        B.next = C

        self.assertEqual(Head.next, A)
        self.assertEqual(C.next, None)



