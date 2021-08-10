"""

Given a binary tree and an integer S, check whether there is root to leaf path with its sum as S.

Example 1:

Input:
Tree = 
            1
          /   \
        2      3
S = 2

Output: 0

Explanation:
There is no root to leaf path with sum 2.
Example 2:

Input:
Tree = 
            1
          /   \
        2      3
S = 4

Output: 1

Explanation:
The sum of path from leaf node 3 to root 1 is 4.

Your Task:  
You dont need to read input or print anything. Complete the function hasPathSum() which takes root node and target sum S as input parameter and returns true if path exists otherwise it returns false.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(height of tree)

Constraints:
1 ≤ N ≤ 10^4
1 ≤ S ≤ 10^6

"""

# Time Complexity: O(n)

class Solution:
    def hasPathSum(self, root, S):
        ans = False
        subSum = S - root.data

        if (subSum == 0 and root.left == None and root.right == None):
            return True

        if root.left is not None:
            ans = ans or self.hasPathSum(root.left, subSum)

        if root.right is not None:
            ans = ans or self.hasPathSum(root.right, subSum)

        return ans

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

s = 2
root = Node(1)
root.left = Node(2)
root.right = Node(3)

if Solution().hasPathSum(root, s):
    print ("There is a root-to-leaf path with sum %d" % (s))
else:
    print ("There is no root-to-leaf path with sum %d" % (s))