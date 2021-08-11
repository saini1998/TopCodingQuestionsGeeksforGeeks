"""

Given an array of N positive integers, print k largest elements from the array. 

Example 1:

Input:
N = 5, k = 2
arr[] = {12,5,787,1,23}
Output: 787 23
Explanation: First largest element in
the array is 787 and the second largest
is 23.
Example 2:

Input:
N = 7, k = 3
arr[] = {1,23,12,9,30,2,50}
Output: 50 30 23
Explanation: Three Largest element in
the array are 50, 30 and 23.
Your Task:
Complete the function kLargest() that takes the array, N and K as input parameters and returns a list of k largest element in descending order. 

Expected Time Complexity: O(N log K)
Expected Auxiliary Space: O(K)

Constraints:
1 ≤ N ≤ 104
K ≤ N
1 ≤ array[i] ≤ 105

"""

"""

This method is mainly an optimization of method 1. Instead of using temp[] array, use Min Heap.
1) Build a Min Heap MH of the first k elements (arr[0] to arr[k-1]) of the given array. O(log(k))
2) For each element, after the kth element (arr[k] to arr[n-1]), compare it with root of MH. 
……a) If the element is greater than the root then make it root and call heapify for MH 
……b) Else ignore it. 
// The step 2 is O((n-k)*log(k))
3) Finally, MH has k largest elements and root of the MH is the kth largest element.
Time Complexity: O(log(k) + (n-k)*log(k)) without sorted output. If sorted output is needed then O(log(k) + (n-k)*log(k) + k*log(k))

"""

class Solution:
    def kLargest(self,li,n,k):
        maxHeap = []

        for i in range(k):
            maxHeap.append(li[i])
            
        for i in range(k,n):
            maxHeap.sort(reverse = True)
            if (li[i] < maxHeap[k-1]):
                continue
            
            else:
                maxHeap.pop(k-1)
                maxHeap.append(li[i])
        
        # maxHeap.sort(reverse=True)
        return maxHeap

for t in range(int(input())):
    li = [int(x) for x in input().strip().split()]
    n, k = li[0], li[1]
    li = [int(x) for x in input().strip().split()]
    ob = Solution()
    kLL = ob.kLargest(li, n, k)

    for element in kLL:
        print(element, end=' ')

    print('')