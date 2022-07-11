"""

Given a binary tree, print the bottom view from left to right.
A node is included in bottom view if it can be seen when we look at the tree from bottom.

                      20
                    /    \
                  8       22
                /   \        \
              5      3       25
                    /   \      
                  10    14

For the above tree, the bottom view is 5 10 3 14 25.
If there are multiple bottom-most nodes for a horizontal distance from root, then print the later one in level traversal. For example, in the below diagram, 3 and 4 are both the bottommost nodes at horizontal distance 0, we need to print 4.

                      20
                    /    \
                  8       22
                /   \     /   \
              5      3 4     25
                     /    \      
                 10       14

For the above tree the output should be 5 10 4 14 25.
 

Example 1:

Input:
       1
     /   \
    3     2
Output: 3 1 2
Explanation:
First case represents a tree with 3 nodes
and 2 edges where root is 1, left child of
1 is 3 and right child of 1 is 2.

Thus nodes of the binary tree will be
printed as such 3 1 2.
Example 2:

Input:
         10
       /    \
      20    30
     /  \
    40   60
Output: 40 20 60 30
Your Task:
This is a functional problem, you don't need to care about input, just complete the function bottomView() which takes the root node of the tree as input and returns an array containing the bottom view of the given tree.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= Number of nodes <= 105
1 <= Data of a node <= 105

"""

class Solution:

    def bottomView(self, root):
        d = dict()
        self.bottomViewUtil(root, d, 0, 0)
        
        result = []
        for i in sorted(d.keys()):
            result.append(d[i][0])
        
        return result
            
    def bottomViewUtil(self, root, d, hd, level):
        if root is None:
            return
        
        if hd in d:
            if level >= d[hd][1]:
                d[hd] = [root.data, level]
        else:
            d[hd] = [root.data, level]
            
        self.bottomViewUtil(root.left, d, hd-1, level+1)
        self.bottomViewUtil(root.right, d, hd+1, level+1)
        



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
        answer = Solution().bottomView(root)
        print(answer)
        print()