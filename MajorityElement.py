"""
Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears more than N/2 times in the array.
 

Example 1:

Input:
N = 3 
A[] = {1,2,3} 
Output:
-1
Explanation:
Since, each element in 
{1,2,3} appears only once so there 
is no majority element.
Example 2:

Input:
N = 5 
A[] = {3,1,3,3,2} 
Output:
3
Explanation:
Since, 3 is present more
than N/2 times, so it is 
the majority element.

Your Task:
The task is to complete the function majorityElement() which returns the majority element in the array. If no majority exists, return -1.
 

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
 

Constraints:
1 ≤ N ≤ 107
0 ≤ Ai ≤ 106

"""

"""
-------------------------------------> Hashmap Solution

Time Complexity = O(n)
One traversal of the array is needed, so the time complexity is linear.

Space Complexity = O(n)
Since a hashmap requires linear space.

"""

class Solution:
    def majorityElement(self, A, N):
        m = {}
        for i in range(N):
            if A[i] in m:
                m[A[i]] += 1
            else:
                m[A[i]] = 1
        
        count = 0
        for key in m:
            if m[key] > N/2:
                count = 1
                return key
        
        if count == 0:
            return -1

# Driver code 
arr = [2, 2, 2, 2, 5, 5, 2, 3, 3] 
n = len(arr)

N = 5
A = [3,1,3,3,2]

print("Solution = " + str(Solution().majorityElement(arr,n)))