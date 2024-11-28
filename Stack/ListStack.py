class ListStack:
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        if len(self.stack) == 0:
            raise IndexError("Pop from empty stack")
        return self.stack.pop()
    
    def peek(self):
        if len(self.stack) == 0:
            raise IndexError("Stack is Empty")
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    