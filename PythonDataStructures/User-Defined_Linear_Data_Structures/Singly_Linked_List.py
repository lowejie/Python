# Linked List is a linear data structure featuring a collection of nodes stored randomly.
# Each node contains data and reference(pointer to address of next node)

# Node Creation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# node1 = Node(8)
# print(node1.data)
# print(node1.next)

# Linked List Creation


class SinglyLL:
    def __init__(self):
        self.head = None


singly_linked_list = SinglyLL()  # sLL.head = None
print(singly_linked_list.head)


# Traversal, Insertion and Deletion in Linked List

class Node:
  def __init__(self,data):
    self.data = data #n1.data=5, n2.data = 10, n3.data = 15, n4.data = 20, nb.data=2
    self.next = None #n1.next = None, n2.next=None, n3.next = None,n4.next = None, nb.next=None

class Sll:
  def __init__(self):
    self.head = None #sll.head = None

  def traversal(self):
    if self.head == None:
      print("linked list is empty")
    else:
      a = self.head     #a=sll.head
      while a != None:  #a=sll.head=n1      #a=n1.next
        print(a.data, end=" ")  #a.data=n1.data, n2.data
        a = a.next              #a=n1.next, a=n2.next

  def insert_at_beginning(self, data):
    print()
    nb = Node(data)  # nb=Node(2)
    nb.next = self.head  # nb.next=n1
    self.head = nb  # sll.head = nb

  def insert_at_end(self, data):  # data=25
    print()
    ne = Node(data)
    a = self.head  # a = sll.head=nb
    while a.next != None:  # a.next=nb.next
      a = a.next  # a=nb.next=n1
    a.next = ne

  def insert_at_specified_node(self, position, data):  # position=3, data=7
    print()
    nib = Node(data)
    a = self.head  # sll.head = nb
    for i in range(1, position - 1):
      a = a.next  # a=nb.next=n1
    nib.next = a.next  # nib.next=n1.next
    a.next = nib  # a.next=n1.next=nib

  def deletion_at_beginning(self):
    print()
    a = self.head
    self.head = a.next
    a.next = None

  def deletion_at_end(self):
    print()
    prev = self.head
    a = self.head.next
    while a.next != None:
      a = a.next
      prev = prev.next
    prev.next = None

  def deletion_at_particular_node(self, position):
    print()
    prev = self.head
    a = self.head.next
    for i in range(1, position - 1):
      a = a.next
      prev = prev.next
    prev.next = a.next
    a.next = None


n1 = Node(5)
sll = Sll()
sll.head = n1
n2 = Node(10)
n1.next = n2
n3 = Node(15)
n2.next = n3
n4 = Node(20)
n3.next = n4
print("Singly Linked List:")
sll.traversal()
sll.insert_at_beginning(2)
print("Singly Linked List after insertion at beginning:")
sll.traversal()
sll.insert_at_end(25)
print("Singly Linked List after insertion at end:")
sll.traversal()
sll.insert_at_specified_node(3,7)
print("Singly Linked List after insertion at position 3:")
sll.traversal()
sll.deletion_at_beginning()
print("Singly Linked List after deletion at beginning:")
sll.traversal()
sll.deletion_at_end()
print("Singly Linked List after deletion at end:")
sll.traversal()
sll.deletion_at_particular_node(3)
print("Singly Linked List after deletion at position 3:")
sll.traversal()