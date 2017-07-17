## Rohan's Implementation of a Single Linked List
## Created July 16th 2017
## Credits: https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/

####### Initializing the Node #########################
#each node has data and a pointer to the next node
#1 - An empty list has a NULL node (basically nothing in it - empty)
#2 - we can get the data of the node
#3 - we can get what the node points to
#4 - we can reset what the node points to

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
    ## Size ## - 
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count
    
