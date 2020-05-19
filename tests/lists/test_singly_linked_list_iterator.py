import unittest

from aed_ds.lists.singly_linked_list import SinglyLinkedList
from aed_ds.exceptions import NoSuchElementException

class TestSinglyLinkedListIterator(unittest.TestCase):
    def setUp(self):
        def setUp(self):
        self.singly_linked_list = SinglyLinkedList()
    
    def add_elements(self, quantity):
        for i in range(quantity):
            self.singly_linked_list.insert_last(f'element {i + 1}')

    def test_has_next(self):
        it = self.singly_linked_list.iterator()
        self.assertFalse(it.has_next())
        self.add_elements(3)
        it = self.singly_linked_list.iterator()
        self.assertTrue(it.has_next())
        it.next()
        self.assertTrue(it.has_next())
        it.next()
        self.assertTrue(it.has_next())
        it.next()
        self.assertFalse(it.has_next())

    def test_next(self):
        it = self.singly_linked_list.iterator()
        with self.assertRaises(NoSuchElementException):
            it.next()
        self.add_elements(3)
        it = self.singly_linked_list.iterator()
        self.assertEqual(it.next(), "element 1")
        self.assertEqual(it.next(), "element 2")
        self.assertEqual(it.next(), "element 3")
        with self.assertRaises(NoSuchElementException):
            it.next()

    def test_rewind(self):
        self.add_elements(3)
        it = self.singly_linked_list.iterator()
        self.assertEqual(it.next(), "element 1")
        self.assertEqual(it.next(), "element 2")
        it.rewind()
        self.assertEqual(it.next(), "element 1")
