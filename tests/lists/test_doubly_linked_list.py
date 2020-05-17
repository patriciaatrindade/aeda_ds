import unittest

from aed_ds.lists.doubly_linked_list import DoublyLinkedList
from aed_ds.tad_iterator import TwoWayIterator
from aed_ds.exceptions import *

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = DoublyLinkedList()

    def test_insert_first(self):
        self.list.insert_first("element 1")
        self.assertEqual(self.list.get(0), "element 1")
        self.list.insert_first("element 2")
        self.list.insert_first("element 3")
        self.list.insert_first("element 4")
        self.list.insert_first("element 5")
        self.assertEqual(self.list.get(0), "element 5")

    def test_insert_last(self):
        self.list.insert_last("element 1")
        self.assertEqual(self.list.get(0), "element 1")
        self.list.insert_last("element 2")
        self.list.insert_last("element 3")
        self.list.insert_last("element 4")
        self.list.insert_last("element 5")
        self.assertEqual(self.list.get(4), "element 5")

    def test_insert_first_and_last(self):
        self.list = DoublyLinkedList()
        self.list.insert_first("element 1")
        self.list.insert_last("element 2")
        self.assertEqual(self.list.get(0), "element 1")
        self.assertEqual(self.list.get(1), "element 2")
    
    # def test_insert(self): pass

    # def test_remove_first(self): pass

    # def test_remove_last(self): pass

    # def test_remove(self): pass

    def test_iterator(self):
        self.assertIsInstance(self.list.iterator(), TwoWayIterator)