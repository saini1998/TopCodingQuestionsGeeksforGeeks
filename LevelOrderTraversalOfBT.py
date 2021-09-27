"""

Given the root of a binary tree, display the node values at each level. Node values for all levels should be displayed on separate lines. 

Runtime complexity: Linear, O(n)
Memory Complexity: Linear, O(n)

"""
class Node:
    def __init__(self ,key):
        self.data = key
        self.left = None
        self.right = None
 

def printLevelOrder(root):
    # Base Case
    if root is None:
        return
     
    # Create an empty queue
    # for level order traversal
    queue = []
 
    # Enqueue Root and initialize height
    queue.append(root)
 
    while(len(queue) > 0):
       
        # Print front of queue and
        # remove it from queue
        print (queue[0].data, end=' ')
        node = queue.pop(0)
 
        #Enqueue left child
        if node.left is not None:
            queue.append(node.left)
 
        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)
 
#Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print ("Level Order Traversal(BFS) of binary tree is -")
printLevelOrder(root)