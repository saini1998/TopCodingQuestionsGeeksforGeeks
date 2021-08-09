"""

Given a binary tree. Check whether it is a BST or not.
Note: We are considering that BSTs can not contain duplicate Nodes.

Example 1:

Input:
    2
 /    \
1      3
Output: 1 
Explanation: 
The left subtree of root node contains node 
with key lesser than the root node’s key and 
the right subtree of root node contains node 
with key greater than the root node’s key.
Hence, the tree is a BST.
Example 2:

Input:
  2
   \
    7
     \
      6
       \
        5
         \
          9
           \
            2
             \
              6
Output: 0 
Explanation: 
Since the node with value 7 has right subtree 
nodes with keys less than 7, this is not a BST.
Your Task:
You don't need to read input or print anything. Your task is to complete the function isBST() which takes the root of the tree as a parameter and returns true if the given binary tree is BST, else returns false. 

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the BST).

Constraints:
0 <= Number of edges <= 100000

"""

"""
            Time Complexity: O(n) 
            Auxiliary Space: O(1) if Function Call Stack size is not considered, otherwise O(n)
"""

class Node:
    def __init__(self, value):
        self.data = value
        self.right = None
        self.left = None

class Solution:
    
    def inOrderTraversal(self, root, newList):
        if not root:
            return
        
        self.inOrderTraversal(root.left, newList)
        newList.append(root.data)
        self.inOrderTraversal(root.right, newList)
    
    def isBST(self, root):
        newList = []
        self.inOrderTraversal(root, newList)
        for i in range(len(newList) - 1):
            if newList[i] >= newList[i+1]:
                return 0
                
        return 1

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

anotherRoot = Node(2)
anotherRoot.right = Node(7)
anotherRoot.right.right = Node(6)
anotherRoot.right.right.right = Node(5)
anotherRoot.right.right.right.right = Node(9)
anotherRoot.right.right.right.right.right = Node(2)
anotherRoot.right.right.right.right.right.right = Node(6)

obj = Solution()
if obj.isBST(root):
    print("isBST")

else:
    print("isNotBST")

print("test with another root")

if obj.isBST(anotherRoot):
    print("isBST")

else:
    print("isNotBST")