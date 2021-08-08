"""
Given a sorted and rotated array A of N distinct elements which is rotated at some point, and given an element key. The task is to find the index of the given element key in the array A.

Example 1:

Input:
N = 9
A[] = {5, 6, 7, 8, 9, 10, 1, 2, 3}
key = 10
Output:
5
Explanation: 10 is found at index 5.
Example 2:

Input:
N = 4
A[] = {3, 5, 1, 2}
key = 6
Output:
-1
Explanation: There is no element that has value 6.
Your Task:
Complete the function search() which takes an array arr[] and start, end index of the array and the K as input parameters, and returns the answer.

Can you solve it in expected time complexity?

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 107
0 ≤ A[i] ≤ 108
1 ≤ key ≤ 108

"""

"""

  -------------------------------->  Recursion Solution
    Time Complexity: O(log n). 
    Binary Search requires log n comparisons to find the element. So time complexity is O(log n).
    Space Complexity: O(1). 
    As no extra space is required.

"""

class Solution:
    def search(self, A : list, l : int, h : int, key : int):
        if l>h:
            return -1
            
        mid = (l+h) // 2
        if A[mid] == key:
            return mid
        
        if A[l] < A[mid]:
            if key >= A[l] and key <= A[mid]:
                return self.search(A, l, mid-1, key)
            return self.search(A, mid+1, h, key)
            
        if key >= A[mid] and key <= A[h]:
            return self.search(A, mid+1, h, key)
        
        return self.search(A, l, mid-1, key)


N = 9
A = [5,6,7,8,9,10,1,2,3]
key = 10
l = 0
h = N-1

print(Solution().search(A,l,h,key))
