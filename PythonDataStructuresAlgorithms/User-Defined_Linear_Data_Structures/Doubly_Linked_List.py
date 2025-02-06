# Doubly Linked Lists are collection of nodes containing data and two pointers.
# One points to previous node and the other points to next node.

class Node:
  def __init__(self,data):  # n1,5            #n2,10
    self.data = data        # n1.data = 5     #n2.data = 10
    self.next = None        # n1.next = None  #n2.next = None
    self.prev = None        # n1.prev = None  #n2.prev = None

class Dll:
    def __init__(self):
        self.head = None   #dll.head = None

    def forward_traversal(self):
        if self.head == None:
            print("doublylinked list is empty")
        else:
            a = self.head
        while a != None:
            print(a.data, end=" ")
            a = a.next

    def backward_traversal(self):
        if self.head == None:
            print("doubly linked list is empty")
        else:
            a = self.head              # dll.head = n1
            while a.next is not None:  #n1.next
                a=a.next               # a = n2    # a= n4
            while a != None:
                print(a.data, end=" ")
                a = a.prev             # a = n4.prev

    def insertion_at_beginning(self, data):
        ns=Node(data)
        a=self.head
        a.prev=ns
        ns.next=a
        self.head=ns

    def insertion_at_end(self, data):
        ne=Node(data)
        a=self.head
        while a.next != None:
            a=a.next
        a.next=ne
        ne.prev=a

    def insertion_at_specified_node(self, position, data):
        nib=Node(data)
        a=self.head
        for i in range(1, position-1):
            a=a.next
        nib.prev = a
        nib.next = a.next
        a.next.prev = nib
        a.next = nib

    def deletion_at_beginning(self):
        a=self.head
        self.head=a.next
        a.next=None
        self.head.prev=None

    def deletion_at_end(self):
        prev=self.head
        a=self.head.next
        while a.next != None:
            a=a.next
            prev=prev.next
        prev.next=None
        a.prev=None

    def deletion_at_particular_node(self, position):
        a=self.head.next
        b=self.head
        for i in range(1,position-1):
            a=a.next
            b=b.next
        b.next=a.next
        a.next.prev=b
        a.next=None
        a.prev=None


n1 = Node(5)
dll = Dll()
dll.head = n1
n2 = Node(10)
n2.prev = n1
n1.next = n2
n3 = Node(15)
n3.prev = n2
n2.next = n3
n4 = Node(20)
n4.prev = n3
n3.next = n4
print("Doubly Linked List Forward Traversal:")
dll.forward_traversal()
print()
print("Doubly Linked List Backward Traversal:")
dll.backward_traversal()
print()
dll.insertion_at_beginning(2)
print("Doubly Linked List Insertion at Beginning:")
dll.forward_traversal()
print()
dll.backward_traversal()
print()
dll.insertion_at_end(25)
print("Doubly Linked List Insertion at end:")
dll.forward_traversal()
print()
dll.backward_traversal()
print()
dll.insertion_at_specified_node(3,7)
print("Doubly Linked List Insertion at position 3:")
dll.forward_traversal()
print()
dll.backward_traversal()
print()
dll.deletion_at_beginning()
print("Doubly Linked List Deletion at Beginning:")
dll.forward_traversal()
print()
dll.backward_traversal()
print()
dll.deletion_at_end()
print("Doubly Linked List Deletion at End:")
dll.forward_traversal()
print()
dll.backward_traversal()
print()
dll.deletion_at_particular_node(3)
print("Doubly Linked List Deletion at Position 3:")
dll.forward_traversal()
print()
dll.backward_traversal()