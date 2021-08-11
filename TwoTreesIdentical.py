"""

Given two binary trees, the task is to find if both of them are identical or not. 


Example 2:

Input:
     1          1
   /   \      /   \
  2     3    2     3
Output: Yes
Explanation: There are two trees both
having 3 nodes and 2 edges, both trees
are identical having the root as 1,
left child of 1 is 2 and right child
of 1 is 3.
Example 2:

Input:
    1       1
  /  \     /  \
 2    3   3    2
Output: No
Explanation: There are two trees both
having 3 nodes and 2 edges, but both
trees are not identical.

Your task:
Since this is a functional problem you don't have to worry about input, you just have to complete the function isIdentical() that takes two roots as parameters and returns true or false. The printing is done by the driver code.


Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).


Constraints:
1 <= Number of nodes <= 105
1 <=Data of a node <= 105

"""

class Solution:
    def isIdentical(self,root1, root2):
        if root1 is None and root2 is None:
            return True
            
        if root1 is not None and root2 is not None:
            return ( 
                (root1.data == root2.data) 
                and 
                self.isIdentical(root1.left, root2.left) 
                and 
                self.isIdentical(root1.right, root2.right) 
            )
            
        return False

from collections import deque

class Node:
    def __init__(self, value):
        self.data = value
        self.right = None
        self.left = None

def inOrderTraversal(root):
    if root is None:
        return None
    inOrderTraversal(root.left)
    print(root.data, end=' ')
    inOrderTraversal(root.right)

def buildTree(s):
    if (len(s) == 0 or s[0] == 'N'):
        return None
    
    ip = list(map(str, s.split()))

    root = Node(int(ip[0]))
    size = 0
    q = deque()

    q.append(root)
    size += 1

    i = 1
    while (size>0 and i<len(ip)):
        currNode = q[0]
        q.popleft()
        size -= 1

        currVal = ip[i]

        if currVal != 'N':
            currNode.left = Node(int(currVal))
            q.append(currNode.left)
            size += 1
        
        i += 1

        if (i>=len(ip)):
            break
        currVal = ip[i]

        if currVal != 'N':
            currNode.right = Node(int(currVal))
            q.append(currNode.right)
            size += 1

        i += 1
    
    return root

if __name__ == '__main__':
    for _ in range(int(input())):
        s1 = input()
        s2 = input()
        h1 = buildTree(s1)
        h2 = buildTree(s2)
        inOrderTraversal(h1)
        print()
        inOrderTraversal(h2)
        print('')
        if Solution().isIdentical(h1,h2):
            print("Fuck yeah baby")
        else:
            print("no you idiot")
        
        print('')
