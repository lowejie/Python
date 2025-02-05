# Queue is a linear data structure following First In First Out (FIFO) order
# Insertion from rear end and Deletion from front end.

# List Implementation
stock_price_queue = []
stock_price_queue.insert(0,131)
stock_price_queue.insert(0,132)
stock_price_queue.insert(0,135)
print(stock_price_queue)

stock_price_queue.pop()
print(stock_price_queue)
stock_price_queue.pop()
print(stock_price_queue)
stock_price_queue.pop()
print(stock_price_queue)

# collections.deque Implementation

from collections import deque
queue = deque()
queue.appendleft(5)
queue.appendleft(12)
queue.appendleft(32)
print(queue)
queue.pop()
print(queue)
queue.pop()
print(queue)
queue.pop()
print(queue)

# Queue Class Implementation using collections.deque

from collections import deque


class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


queue1 = Queue()

queue1.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
queue1.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
queue1.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})

print(queue1.size())
print(queue1.dequeue())
print(queue1.dequeue())
print(queue1.dequeue())