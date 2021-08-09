"""

Given an integer N, our task is to print N distinct numbers such that their sum is 0.
Examples:
 

Input: N = 3 
Output: 1, -1, 0 
Explanation: 
On adding the numbers that is 1 + (-1) + 0 the sum is 0.
Input: N = 4 
Output: 1, -1, 2, -2 
Explanation: 
On adding the numbers that is 1 + (-1) + 2 + (-2) the sum is 0. 

"""

# Time Complexity for Sum() = O(n)
# Time Complexity for Append() = O(1)

class Solution:
    def findNumbers(self, N):

        arr = list(range(1,N))
        arr.append(-sum(arr))

        return arr

N = 4

print(Solution().findNumbers(N))

