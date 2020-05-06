from list import List
#import nodes as n 
from nodes import SingleListNode as sln

# import sys
# sys.path.append('..')
# from exceptions import EmptyListException, InvalidPositionException, NoSuchElementException


class single_linked_list(list):

    def __init__(self):
        self.head = None
        self.tail = None 
        self.num_elements = 0
    
    # Returns true iff the list contains no elements.
    def is_empty(self): 
        if self.head is None:
            return True 
        return False

    # Returns the number of elements in the list.
    def size(self):
        return self.num_elements 

    # Returns the first element of the list.
    # Throws EmptyListException.
    def get_first(self):    
        try:    
            if not self.head:
                raise Exception
            else:
                return self.head.get_element()
        except:
            EmptyListException()


    # Returns the last element of the list.
    # Throws EmptyListException.
    def get_last(self): 
        try:
            if self.tail:
                return self.tail.get_element()
            else:
                raise Exception
        except:
            return ("EmptyListException")

    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    
    def get(self, position): 
        buscar_node = self.head
        if position < 0 or position > self.size():
            print("Posicao invalida ou lista inexistente") # é suposto fazer raise InvalidPosition?
        else:
           index = 0
           cur_node = self.head
           while position > index:
               cur_node = cur_node.next_node
               index += 1
        return cur_node.get_element()


    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.
    def find(self, element): 
        cur_node = self.head
        index = 0
        while cur_node:
            if element == cur_node.get_element():
              return index
            cur_node = cur_node.next_node
            index += 1
        return -1

    # Inserts the specified element at the first position in the list.
    def insert_first(self, element):
        new_node = sln(element, self.head)  # cria-se um novo nó
        if not self.head:
            self.tail = new_node 
        self.head = new_node
        self.num_elements += 1

    # Inserts the specified element at the last position in the list.
    def insert_last(self, element):  
        node = sln (element, None)  
        if self.tail == None:
            node.set_next(None)
            self.tail = self.head = node 
        else:
            self.tail.set_next(node) #o meu last é que vai ser o meu nó
            self.tail = node
            self.num_elements +=1

    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.

    def insert(self, element, position): 
        try:
            if position < 0:
                raise Exception                
            elif position == 0:
                self.insert_first(element)
            elif position == self.num_elements:
                self.insert_last(element)
            else:
                new_node = self.head
                index = 0
                while new_node:
                    index += 1
                    if index == position:
                        new_node.next_node = sln(element, new_node.next_node)
                        self.num_elements += 1
                        break
        except:
            print("InvalidPosition!")


    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
    def remove_first(self): 
        try:
            if self.head:
                primeiro = self.head
                self.head = self.head.next_node
                self.num_elements -= 1
                return primeiro.get_element()
            else:
                raise Exception
        except:
            return ("EmptyListException")

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    def remove_last(self): 
        try:
            if not self.head:
                raise Exception
            else:
                ultimo = self.head
                while (ultimo.next_node is not None):
                    prev = ultimo
                    ultimo = ultimo.next_node
                prev.next_node = None
                self.num_elements -= 1
                return ultimo.get_element()

        except:
            return ("EmptyListException")
    
    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
    def remove(self, position): 
        try:
            if not self.head:
                raise Exception
            else:
                node_to_remove = self.head
                previous_node = None
                index = 0
                while node_to_remove:
                    if index == position - 1:
                        previous_node = node_to_remove
                        node_to_remove = node_to_remove.next_node
                        old_node = node_to_remove
                        previous_node.set_next(node_to_remove.next_node)
                        return old_node.get_element()
                    node_to_remove = node_to_remove.next_node
                    index += 1
        except:
            InvalidPositionException

    
    # Removes all elements from the list.
    def make_empty(self): 
        self.head = None
        self.tail = None 
        self.num_elements = 0

    # Returns an iterator of the elements in the list (in proper sequence).
    def iterator(self): pass
        
        
    def print_list(self):
        current_node = self.head
        if self.head:
            print(f'Head: {self.head.get_element()}') 
            print(f'Tail: {self.tail.get_element()}')
        while current_node:
            print(current_node.element)
            current_node = current_node.next_node

    


llist = single_linked_list()


llist.insert_first("C")
llist.insert_first("A")


llist.insert_last("D")
llist.insert("B",1)
llist.insert("E",4)

# size
print(llist.size())

#find_method
print(llist.find("C"))
print(llist.find("D"))

#get_method
print(f'Position: 1, element: {llist.get(1)}')

#get_first_method
print(f'get first: {llist.get_first()}')

# get last method
print(f'get last: {llist.get_last()}')

# get method from position
# print(llist.get(3))

#remove_last_node erro
print(llist.remove_last())

#remove_first_node
print(llist.remove_first())

#remove_node erro
print(llist.remove(1))

#iterator
#llist.iterator()

llist.print_list()

