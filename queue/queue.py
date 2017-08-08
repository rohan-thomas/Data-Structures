## Rohan's Implementation of a Single Linked List
## Created August 6th 2017

class Node(object):
    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node
    def get_data(self):
        return self.data
    def get_next_node(self):
        return self.next_node
    def point_to(self,new_next_node):
        self.next_node=new_next_node

class Queue(object):
    def __init__(self,head=None,tail=None):
        self.head=head
        self.tail=tail

    def enqueue(self,data):
        new_node = Node(data)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.point_to(self.head)
            self.head = new_node

    def size_of_queue(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next_node()
        return count

    def get_tail(self):
        if self.tail == None:
            return "The Queue is Empty"
        else:
            return self.tail.get_data()
            
    def get_head(self):
        if self.tail == None:
            return "The Queue is Empty"
        else:
            return self.head.get_data()
          
    def dequeue(self):
        current = self.head
        condition = False
        while current and condition is False:
            if self.head == None and self.tail == None:
                return "EMPTY"
            elif self.head == self.tail:
                temp = self.head.get_data()
                self.head = None
                self.tail = None
                return "DELETING:",temp
            elif current.get_next_node() is None:
                condition = True
                self.tail = previous
                previous.point_to(current.get_next_node())
                return "DELETING:",current.get_data()
            else:
                previous = current
                current = current.get_next_node()
        


        


NEWQUEUE = Queue()
print(NEWQUEUE.dequeue())
#print(NEWQUEUE.dequeue())
NEWQUEUE.enqueue("rohan")
NEWQUEUE.enqueue("mani")
NEWQUEUE.enqueue("thomas")
NEWQUEUE.enqueue("1")
print(NEWQUEUE.size_of_queue())

print("NEXT UP: ",NEWQUEUE.get_tail())
print(NEWQUEUE.dequeue())
print("END: ",NEWQUEUE.get_head())

print("NEXT UP: ",NEWQUEUE.get_tail())
print(NEWQUEUE.dequeue())
print("END: ",NEWQUEUE.get_head())

print("NEXT UP: ",NEWQUEUE.get_tail())
print(NEWQUEUE.dequeue())
print("END: ",NEWQUEUE.get_head())

print("NEXT UP: ",NEWQUEUE.get_tail())
print(NEWQUEUE.dequeue())
print("END: ",NEWQUEUE.get_head())

print("NEXT UP: ",NEWQUEUE.get_tail())
print(NEWQUEUE.dequeue())
print("END: ",NEWQUEUE.get_head())
'''
#print("HEAD: ", NEWQUEUE.get_head())
print("TAIL: ", NEWQUEUE.get_tail())

print(NEWQUEUE.dequeue())
print(NEWQUEUE.size_of_queue())
#print("HEAD: ", NEWQUEUE.get_head())
print("TAIL: ", NEWQUEUE.get_tail())
print(NEWQUEUE.dequeue())
print(NEWQUEUE.size_of_queue())
#print("HEAD: ", NEWQUEUE.get_head())
print("TAIL: ", NEWQUEUE.get_tail())
print(NEWQUEUE.dequeue())
print(NEWQUEUE.size_of_queue())
#print("HEAD: ", NEWQUEUE.get_head())
print("TAIL: ", NEWQUEUE.get_tail())
print(NEWQUEUE.dequeue())
print(NEWQUEUE.size_of_queue())
#print("HEAD: ", NEWQUEUE.get_head())
#print("TAIL: ", NEWQUEUE.get_tail())
print(NEWQUEUE.size_of_queue())
'''
