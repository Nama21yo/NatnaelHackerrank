# It is better to implement stack using deque- 
# since it is a double linked list it won't allocate the memory again
from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()
    def push(self, val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)
s = Stack()
s.push(5)
s.push(42)
s.push(246)
s.push(634)
s.push(35)
print(s.peek())
print(s.size())
