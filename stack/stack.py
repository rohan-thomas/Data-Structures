## Rohan's Implementation of a Stack
## Created July 27th 2017
## Credits: http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaStackinPython.html

class Stack():
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[len(self.items)-1]

### My test area
rohan = Stack()
print(rohan.isEmpty())
rohan.push("a")
print(rohan.size())
print(rohan.peek())
rohan.push("b")
print(rohan.size())
print(rohan.peek())
rohan.push("c")
print(rohan.size())
print(rohan.peek())
rohan.push("d")
print(rohan.size())
print(rohan.peek())