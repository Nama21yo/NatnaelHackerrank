class ListQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, val):
        self.queue.append(val)
    
    def dequeue(self):
        # This operation isn't good it will take O(n) time
        return self.queue.pop(0)
    
    def peek(self):
        return self.queue[0]
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return len(self) == 0

class ListQueueFakeDelete:
    def __init__(self):
        self.front = 0
        self.queue = []
    
    def enqueue(self, val):
        self.queue.append(val)
    
    def peek(self):
        return self.queue[self.front]
    
    def dequeue(self):
        frontDelete = self.peek()
        self.front += 1
        return frontDelete
    # There is something a little odd about this code: it never gets rid of old
    # items after they have been dequeued. Even if it deleted them, it still keeps
    # a place in the list for them. This is a kind of lazy update.
    
    def size(self):
        return len(self.queue) - self.front
    
    def is_empty(self):
        return self.size() == 0