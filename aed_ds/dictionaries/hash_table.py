from .tad_dictionary import Dictionary
from .item import Item
from ..exceptions import NoSuchElementException, DuplicatedKeyException
from ..lists.singly_linked_list import SinglyLinkedList

import ctypes

class HashTable(Dictionary):
    def __init__(self, size=101):
        self.num_items = 0
        self.array_size = size
        self.table = (ctypes.py_object * self.array_size)()

        for i in range(self.array_size):
            self.table[i] = SinglyLinkedList()

    def hash_function(self, key):
        return sum([ord(c) for c in key]) % self.array_size

    def has_key(self, key):
        idx = self.hash_function(key)   
        it = self.table[idx].iterator()
        while it.has_next():
            cur_item = it.next()
            if cur_item.get_key() == key:
                return True
    
    def size(self):
        return self.num_items

    def is_full(self):
        return self.num_items == self.array_size

    def get(self, key):
        idx = self.hash_function(key)
        it = self.table[idx].iterator()
        while it.has_next():
            cur_item = it.next()
            if cur_item.get_key() == key:
                return cur_item.get_value()
        raise NoSuchElementException()

    def insert(self, key, value):
        if self.has_key(key):
            raise DuplicatedKeyException()
        idx = self.hash_function(key)
        item = Item(key, value)
        self.table[idx].insert_last(item)
        self.num_items += 1
                
    def update(self, key, value):
        if not self.has_key(key):
            raise NoSuchElementException()
        idx = self.hash_function(key)
        it = self.table[idx].iterator()
        while it.has_next():
            cur_item = it.next()
            if cur_item.get_key() == key:
                return cur_item.set_value(value)
        
    def remove(self, key):
        if not self.has_key(key):
            raise NoSuchElementException()
        collision_list = self.table[self.hash_function(key)]
        it = collision_list.iterator()
        while it.has_next():
            pos = 0
            cur_item = it.next()
            if cur_item.get_key() == key:
                self.num_items -= 1
                collision_list.remove(pos)
                return cur_item.get_value()
            cur_item = cur_item.net()
            pos += 1
        
    def keys(self):
        list_of_keys = SinglyLinkedList()
        for i in range(int(self.array_size)):
            collision_list = self.table[i]
            it = collision_list.iterator()
            while it.has_next():
                cur_item = it.next()
                if cur_item.get_key():
                    list_of_keys.insert_last(cur_item.get_key())
        return list_of_keys
        
    def values(self):
        list_of_values = SinglyLinkedList()
        for i in range(int(self.array_size)):
            collision_list = self.table[i]
            it = collision_list.iterator()
            while it.has_next():
                cur_item = it.next()
                if cur_item.get_key():
                    list_of_values.insert_last(cur_item.get_value())
        return list_of_values

    def items(self):
        list_of_items = SinglyLinkedList()
        for i in range(int(self.array_size)):
            collision_list = self.table[i]
            it = collision_list.iterator()
            while it.has_next():
                cur_item = it.next()
                if cur_item.get_key():
                    list_of_items.insert_last(cur_item)
        return list_of_items
