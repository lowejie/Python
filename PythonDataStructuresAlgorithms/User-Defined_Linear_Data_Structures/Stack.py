# Stack is a linear data structure following Last In First Out (LIFO) order i
# Insertion and deletion is done at one end.

# List Implementation

stack =[]
stack.append("a")
stack.append("b")
stack.append("c")
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

# Collection.deque

from collections import deque
stack = deque()
stack.append("a")
stack.append("b")
stack.append("c")
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

# Queue

from queue import LifoQueue
stack = LifoQueue(maxsize=3)
stack.put("a")
stack.put("b")
stack.put("c")
print(stack.qsize())
print(stack.full())
print(stack.get())
print(stack.full())