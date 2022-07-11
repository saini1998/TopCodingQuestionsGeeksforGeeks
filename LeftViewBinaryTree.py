"""

Given a Binary Tree, print Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. The task is to complete the function leftView(), which accepts root of the tree as argument.

Left view of following tree is 1 2 4 8.

          1
       /     \
     2        3
   /  \      / \
  4    5    6   7
   \
    8   

Example 1:

Input:
   1
 /  \
3    2
Output: 1 3

Your Task:
You just have to complete the function leftView() that returns an array containing the nodes that are in the left view. The newline is automatically appended by the driver code.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
0 <= Number of nodes <= 100
1 <= Data of a node <= 1000

"""

class Solution:

    def leftViewUtil(self, root, level, maxLevel):
        if root is None:
            return

        if maxLevel[0] < level:
            print(root.data, end=" ")
            maxLevel[0] = level

        self.leftViewUtil(root.left, level+1, maxLevel)
        self.leftViewUtil(root.right, level+1, maxLevel)

    def leftView(self,root):
        maxLevel = [0]
        self.leftViewUtil(root, 1, maxLevel)



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
        Solution().leftView(root)
        print()