from ..tad_iterator import TwoWayIterator
from aed_ds.exceptions import EmptyListException, NoSuchElementException

class DoublyLinkedListIterator(TwoWayIterator):
    def __init__(self, doubly_linked_list):
        self.doubly_linked_list = doubly_linked_list
        self.rewind()

    def has_next(self): 
        return self.current_node != None

    def next(self): 
        if not self.has_next():
            raise NoSuchElementException()
        element = self.current_node.get_element()
        self.current_node = self.current_node.get_next()
        return element        

    def rewind(self): 
        self.current_node = self.doubly_linked_list.head

    def has_previous(self):
        return self.current_node != None
    
    def previous(self): 
        if not self.has_previous():
            raise NoSuchElementException()
        element = self.current_node.get_element()
        self.current_node = self.current_node.get_previous()
        return element

    def full_forward(self): 
        self.current_node = self.doubly_linked_list.tail