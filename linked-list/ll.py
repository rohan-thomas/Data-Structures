## Rohan's Implementation of a Single Linked List
## Created July 16th 2017
## Credits: https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/

####### Initializing the Node #########################
#each node has data and a pointer to the next node
#1 - An empty list has a NULL node (basically nothing in it - empty)
#2 - we can get the data of the node
#3 - we can get what the node points to
#4 - we can reset what the node points to
"""
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
    
    def set_next(self,new_next):
        self.next_node = new_next


class LinkedList(object):
    ## Head of the list ## - top node of the list. Set to none if the list is empty
    def __init__(self, head=None): 
        self.head = head 
    ## Insert ## - insert as a node at top, point to old head, new node is head
    def insert(self,data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    ## Size ## - count each node by going next,next,next...
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count
"""
#
#
#
#
#
#
#
#
#

class ll_node(object):
    def __init__(self, data=None,next_node=None):
        self.data=data
        self.next_node= next_node
    def get_data(self):
        return self.data
    def get_next_node(self):
        return self.next_node
    def repoint(self,new_next_node):
        self.next_node = new_next_node

class ll(object):
    def __init__(self, head=None):
        self.head = head
    def insert_node(self, data):
        inserted = ll_node(data)
        inserted.repoint(self.head)
        self.head = inserted
    def list_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.get_next_node()
        return count
    def search_list(self, data):
        current = self.head
        condition = False
        while current and condition is False:
            if current.get_data() == data:
                condition = True
            else:    
                current = current.get_next_node
        if current == None:
            print("Error: No such value")
    def delete_node(self,data):
        current = self.head
        condition = False
        stored = None
        while current and condition is False:
            if current.get_data() == data:
                condition = True
            else:
                stored = current
                current = current.get_next_node()
            if current == None:
                print("Error: No such value")
            if stored is None:
                self.head = current.get_next_node
            else:
                stored.repoint(current.get_next_node())
             
