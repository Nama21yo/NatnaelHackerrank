class ListDEqueue:
    def __init__(self):
        self.dequeue = []
    
        # addfirst(item) - add item to the front of the deque.
        # addlast(item) - add item to the end of the deque.
        # removefirst(item) - remove and return the first item in the deque.
        # removelast(item) - remove and return the last item in the deque.
        # size - return the number of items in the deque.
    def add_first(self, val):
        self.dequeue.insert(0, val)
    
    def add_last(self, val):
        self.dequeue.append(val)
    
    def remove_first(self):
        return self.dequeue.pop(0)
    def remove_last(self):
        return self.dequeue.pop()

    def size(self):
        return len(self.dequeue)

    def is_empty(self):
        return self.size == 0

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
    
class LinkedListDEqueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def add_front(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.size += 1
    
    def add_rear(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
    
    def remove_front(self):
        if self.is_empty():
            raise IndexError("Remove from empty deque")
        removed_node = self.front
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.size -= 1
        return removed_node.data
    
    def remove_rear(self):
        if self.is_empty():
            raise IndexError("Remove from empty deque")
        removed_node = self.rear
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.size -= 1
        return removed_node.data
    
    def peek_front(self):
        if self.is_empty():
            raise IndexError("Peek from empty deque")
        return self.front.data
    
    def peek_rear(self):
        if self.is_empty():
            raise IndexError("Peek from empty deque")
        return self.rear.data
    
    def is_empty(self):
        return self.size == 0
    
    def size(self):
        return self.size
