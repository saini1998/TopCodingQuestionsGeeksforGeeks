"""
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.


Example 1:

Input:
N = 5
arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which 
is a contiguous subarray.
Example 2:

Input:
N = 4
arr[] = {-1,-2,-3,-4}
Output:
-1
Explanation:
Max subarray sum is -1 
of element (-1)

Your Task:
You don't need to read input or print anything. The task is to complete the function maxSubarraySum() which takes arr and N as input parameters and returns the sum of subarray with maximum sum.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N ≤ 106
-107 ≤ A[i] ≤ 107

"""

"""

  -------------------------------->  DP Solution

"""

class Solution:
    def maxSubArraySum(self,a,size):
        maxSoFar = a[0]
        currMax = a[0]

        start =0
        end = 0
        s = 0
        
        for i in range(1,size):
            currMax = max(a[i],currMax + a[i])
            maxSoFar = max(maxSoFar, currMax)

        return maxSoFar


N = 4
arr = [-1,-2,-3,-4]
ob = Solution()
ans = ob.maxSubArraySum(arr,N)
print(ans)
