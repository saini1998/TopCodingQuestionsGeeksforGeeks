"""
Given an array Arr of N positive integers and another number X. Determine whether or not there exist two elements in Arr whose sum is exactly X.

Example 1:

Input:
N = 6, X = 16
Arr[] = {1, 4, 45, 6, 10, 8}
Output: Yes
Explanation: Arr[3] + Arr[4] = 6 + 10 = 16
Example 2:

Input:
N = 5, X = 10
Arr[] = {1, 2, 4, 3, 6}
Output: Yes
Explanation: Arr[2] + Arr[4] = 4 + 6 = 10
Your Task:
You don't need to read input or print anything. Your task is to complete the function hasArrayTwoCandidates() which takes the array of integers arr, n and x as parameters and returns boolean denoting the answer.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 105
1 ≤ Arr[i] ≤ 105

"""

"""

  -------------------------------->  Hashing Solution

"""

class Solution:
	def hasArrayTwoCandidates(self,arr, n, x):
	    s = set()
	    for i in range(0, n):
	        temp = x - arr[i]
	        if (temp in s):
	            return temp
	            
	        s.add(arr[i])


A = [1, 4, 45, 6, 10, 8]
n = 16

ob =Solution()
ans = ob.hasArrayTwoCandidates(A,len(A),n)

if ans:
    print("Yes")

else:
    print("No")


"""

Complexity Analysis:  


Time Complexity: O(n). 
As the whole array is needed to be traversed only once.
Auxiliary Space: O(n). 
A hash map has been used to store array elements.

"""