"""

Given a Binary Tree, convert it into its mirror.            

Example 1:

Input:
      1
    /  \
   2    3
Output: 2 1 3
Explanation: The tree is
   1    (mirror)  1
 /  \    =>      /  \
3    2          2    3
The inorder of mirror is 2 1 3
Example 2:

Input:
      10
     /  \
    20   30
   /  \
  40  60
Output: 30 10 60 20 40
Explanation: The tree is
      10               10
    /    \  (mirror) /    \
   20    30    =>   30    20
  /  \                   /   \
 40  60                 60   40
The inroder traversal of mirror is
30 10 60 20 40.
Your Task:
Just complete the function mirror() that takes node as paramter  and convert it into its mirror. The printing is done by the driver code only.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 ≤ Number of nodes ≤ 105
1 ≤ Data of a node ≤ 105

"""

class Solution:
    def mirror(self,root):
        if (root == None):
            return
        
        q = []
        q.append(root)
        
        while(len(q)):
            current = q[0]
            q.pop(0)
            current.left, current.right = current.right, current.left
            
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)

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
        s = input()
        root = buildTree(s)
        inOrderTraversal(root)
        print('')
        Solution().mirror(root)
        inOrderTraversal(root)
        print('')

