import unittest

from aed_ds.lists.doubly_linked_list import DoublyLinkedList
from aed_ds.exceptions import NoSuchElementException

class TestDoublyLinkedListIterator(unittest.TestCase):
    def setUp(self): 
        self.doubly_linked_list = DoublyLinkedList()

    def add_elements(self, quantity):
        for i in range(quantity):
            self.doubly_linked_list.insert_last(f'element {i + 1}')

    def test_has_next(self): 
        it = self.doubly_linked_list.iterator()
        self.assertFalse(it.has_next())
        self.add_elements(3)
        it = self.doubly_linked_list.iterator()
        self.assertTrue(it.has_next())
        it.next()
        self.assertTrue(it.has_next())
        it.next()
        self.assertTrue(it.has_next())
        it.next()
        self.assertFalse(it.has_next())
 
    def test_next(self):
        it = self.doubly_linked_list.iterator()
        with self.assertRaises(NoSuchElementException):
            it.next()
        self.add_elements(3)
        it = self.doubly_linked_list.iterator()
        self.assertEqual(it.next(), "element 1")
        self.assertEqual(it.next(), "element 2")
        self.assertEqual(it.next(), "element 3")
        with self.assertRaises(NoSuchElementException):
            it.next()

    def test_rewind(self):
        self.add_elements(3)
        it = self.doubly_linked_list.iterator()
        self.assertEqual(it.next(), "element 1")
        self.assertEqual(it.next(), "element 2")
        it.rewind()
        self.assertEqual(it.next(), "element 1")

    def test_has_previous(self): 
        it = self.doubly_linked_list.iterator()
        self.assertFalse(it.has_previous())
        self.add_elements(3)
        it = self.doubly_linked_list.iterator()
        it.full_forward()
        self.assertTrue(it.has_previous())
        it.previous()
        self.assertTrue(it.has_previous())
        it.previous()
        self.assertTrue(it.has_previous())
        it.previous()
        self.assertFalse(it.has_previous())

    def test_previous(self):
        it = self.doubly_linked_list.iterator()
        with self.assertRaises(NoSuchElementException):
            it.previous()
        self.add_elements(3)
        it = self.doubly_linked_list.iterator()
        it.full_forward()
        self.assertEqual(it.previous(), "element 3")
        self.assertEqual(it.previous(), "element 2")
        self.assertEqual(it.previous(), "element 1")
        with self.assertRaises(NoSuchElementException):
            it.previous()

    def test_full_forward(self): 
        self.add_elements(3)
        it = self.doubly_linked_list.iterator()
        self.assertEqual(it.next(), "element 1")
        self.assertEqual(it.next(), "element 2")
        it.full_forward()
        self.assertEqual(it.previous(), "element 3")