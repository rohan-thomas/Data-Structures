## Rohan's Implementation of a Stack
## Created July 27th 2017

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
    

class Stack(object):
    def __init__(self):
        self.head= None
    def push(self, data):
        new_node = Node(data)
        new_node.point_to(self.head)
        self.head = new_node
    def pop(self):
        temp = self.head
        self.head = self.head.get_next_node()
        if self.head == None:
            print("Nothing below")
        else:
            print("the one under the top is ", self.head.get_data())
        #if self.head.get_data() == None:
        #    print("NULL")
        return temp.get_data()
    def isEmpty(self):
        if self.head==None:
            return True
        else:
            return False
    def size(self):
        current = self.head
        count =0
        while current != None:
            count += 1
            current = current.get_next_node()
        if self.head == None:
            count =0
        return count
    def peek(self):
        if self.head == None:
            temp = None
            print("None")
        else:
            temp = self.head.get_data()
        return temp    


####Test scenario:

NEWSTACK = Stack()
print(NEWSTACK.isEmpty())
NEWSTACK.push("Rohan")
print(NEWSTACK.size())
print(NEWSTACK.peek())
print(NEWSTACK.isEmpty())
print(NEWSTACK.peek())
NEWSTACK.push("Thomas")
print(NEWSTACK.size())
print(NEWSTACK.peek())
NEWSTACK.push("Mani")
print(NEWSTACK.size())
print(NEWSTACK.peek())
NEWSTACK.push(1)
print(NEWSTACK.size())
print(NEWSTACK.peek())
NEWSTACK.push(3422432)
print(NEWSTACK.size())
print(NEWSTACK.peek())
NEWSTACK.push("sdasdjsah")
print(NEWSTACK.size())
print(NEWSTACK.peek())
print("####")
#NEWSTACK.push()
print(NEWSTACK.size())
print(NEWSTACK.peek())
NEWSTACK.pop()
print(NEWSTACK.size())
print(NEWSTACK.peek())
NEWSTACK.pop()
print(NEWSTACK.size())
print(NEWSTACK.peek())
NEWSTACK.pop()
print(NEWSTACK.size())
print(NEWSTACK.peek())
NEWSTACK.pop()
print(NEWSTACK.size())
print(NEWSTACK.peek())
NEWSTACK.pop()
print(NEWSTACK.size())
NEWSTACK.pop()
print(NEWSTACK.size())
NEWSTACK.peek()
