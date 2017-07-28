## Rohan's Implementation of a Single Linked List
## Created July 16th 2017
## Credits: https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/


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

class LinkedList(object):
    def __init__(self,head=None):
        self.head = head
    def insert_node(self,data):
        new_node = Node(data)
        new_node.point_to(self.head)
        self.head = new_node
    def size_of_list(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.get_next_node()
        return count
    def search_list(self,data):
        condition = False
        current = self.head
        while current and condition is False:
            if current.get_data() == data:
                condition = True
            else:
                current = current.get_next_node()
        if current is None:
            raise ValueError("Data not in list")
        return current
    def delete_node(self,data):
        current = self.head
        condition = False
        previous = None
        while current and condition is False:
            if current.get_data() == data:
                condition = True
            else: 
                previous = current
                current = current.get_next_node()
        if current is None:
            raise ValueError("Data not in list")
        elif previous is None:
            self.head = current.get_next_node()
        else:
            previous.point_to(current.get_next_node())

### My messy test area
test = Node(1)
test2 = LinkedList()
test3 = test2.insert_node(test)
print(test.get_data())
print(test2)
print(test2.size_of_list())
tom = Node(2)
test2.insert_node(tom)
print("tom is",tom.get_data())
print(test2.size_of_list())
test2.delete_node(tom)
print(test2.size_of_list())