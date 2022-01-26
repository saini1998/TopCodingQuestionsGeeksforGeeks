"""

Given an array of integers and another number. Find all the unique quadruple from the given array that sums up to the given number.

Example 1:

Input:
N = 5, K = 3
A[] = {0,0,2,1,1}
Output: 0 0 1 2 $
Explanation: Sum of 0, 0, 1, 2 is equal
to K.
Example 2:

Input:
N = 7, K = 23
A[] = {10,2,3,4,5,7,8}
Output: 2 3 8 10 $2 4 7 10 $3 5 7 8 $
Explanation: Sum of 2, 3, 8, 10 = 23,
sum of 2, 4, 7, 10 = 23 and sum of 3,
5, 7, 8 = 23.
Your Task:
You don't need to read input or print anything. Your task is to complete the function fourSum() which takes the array arr[] and the integer k as its input and returns an array containing all the quadruples in a lexicographical manner. Also note that all the quadruples should be internally sorted, ie for any quadruple [q1, q2, q3, q4] the following should follow: q1 <= q2 <= q3 <= q4.  (In the output each quadruple is separate by $. The printing is done by the driver's code)

Expected Time Complexity: O(N3).
Expected Auxiliary Space: O(N2).

Constraints:
1 <= N <= 100
-1000 <= K <= 1000
-100 <= A[] <= 100

"""

def fourSum(nums, target):
        
        ans = set()
        n = len(nums)
        nums.sort()
        for i in range(n):
            for j in range(i+1,n):
                left = j + 1
                right = n - 1
    
                while left < right:
                    total = nums[i] + nums[left] + nums[right]+nums[j]
                    if total > target:
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        ans.add(tuple(sorted((nums[i], nums[left], nums[right],nums[j]))))
                    
                        left += 1
                        right -= 1
        ansList = list(ans)
        ansList.sort()
        return ansList

A = [10,2,3,4,5,7,8]
K = 23

print(fourSum(A, K))