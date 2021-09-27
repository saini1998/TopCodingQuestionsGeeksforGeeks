"""

Convert a binary tree to a doubly linked list so that the order of the doubly linked list is the same as an in-order traversal of the binary tree.

After conversion, the left pointer of the node should be pointing to the previous node in the doubly linked list, and the right pointer should be pointing to the next node in the doubly linked list.

Runtime complexity: Linear, O(n)

Memory Complexity: Linear, O(h)

Recursive solution has O(h) memory complexity as it will consume memory on the stack up to the height of binary tree h. It will be O(logn) for balanced trees and in the worst case can be O(n).

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 

def inorder(root):     
    if root is not None:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)

def fixPrevPtr(root):
    if root is not None:
        fixPrevPtr(root.left)
        root.left = fixPrevPtr.pre
        fixPrevPtr.pre = root
        fixPrevPtr(root.right)

def fixNextPtr(root):
 
    prev = None
    while(root and root.right != None):
        root = root.right

    while(root and root.left != None):
        prev = root
        root = root.left
        root.right = prev
 
    return root
 

def BTToDLL(root):
     
    fixPrevPtr(root)
    return fixNextPtr(root)
 
def printList(root):
    while(root != None):
        print(root.data, end=' ')
        root = root.right
 
# Driver program to test above function
root = Node(10)
root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)
 
print("Inorder Tree Traversal")
inorder(root)
 
# Static variable pre for function fixPrevPtr
fixPrevPtr.pre = None
head = BTToDLL(root)
print("\nDLL Traversal")
printList(head)