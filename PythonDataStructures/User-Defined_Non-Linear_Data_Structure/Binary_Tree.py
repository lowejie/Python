# Can have more than one children
# Two children at most for binary tree
# Topmost element is the root of the tree
# Traversal methods include preorder, postorder, inorder

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def traPreOrder(self):
        print(self.val, end=" ")
        if self.left:
            self.left.traPreOrder()
        if self.right:
            self.right.traPreOrder()

    def traInOrder(self):
        if self.left:
            self.left.traInOrder()
        print(self.val, end=" ")
        if self.right:
            self.right.traInOrder()

    def traPostOrder(self):
        if self.left:
            self.left.traPostOrder()
        if self.right:
            self.right.traPostOrder()
        print(self.val, end=" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print("Pre order traversal: ", end="")
root.traPreOrder()
print()
print("In order traversal: ", end="")
root.traInOrder()
print()
print("Post order traversal: ", end="")
root.traPostOrder()
print()