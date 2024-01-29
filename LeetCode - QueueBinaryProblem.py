from collections import deque

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def front(self):
        return self.buffer[-1]
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)

def produce_binary_numbers(n):
    queue = Queue()
    front = "1"
    queue.enqueue(front)
    for i in range(n):
        front = queue.front()
        print("    " + front)
        queue.enqueue(front + "0")
        queue.enqueue(front + "1")

        queue.dequeue()
        
if __name__ == '__main__':
    produce_binary_numbers(10)

        
