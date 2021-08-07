"""
Given a binary number, Find, if given binary number is a multiple of 3. The given number can be big upto 2^10000. It is recommended to finish the task using one traversal of input binary string.

Example 1:

Input: S = "011"
Output: 1
Explanation: "011" decimal equivalent
is 3, which is divisible by 3.
â€‹Example 2:

Input: S = "100"
Output: 0
Explanation: "100" decimal equivalent
is 4, which is not divisible by 3.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function isDivisible() which takes the string s as inputs and returns 1 if the given number is divisible by 3 otherwise 0.

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ |S| ≤ 105

"""

"""

  -------------------------------->  Type Casting Solution

"""


class Solution:
    def isDivisible(self, s):
        v=int(s,2)
        if v%3==0:
            return 1
        else:
            return 0

"""

  -------------------------------->  Bit Manipulation Solution

"""

class BitManSolution:

    def isMultipleOfThree(self,s):

        oddCount = 0
        evenCount = 0

        n = int(s,2)
        if n<0:
            n = -n
        if n==0:
            return 1
        if n==1:
            return 0
        
        while(n):
            if (n&1):
                oddCount += 1
            if (n&2):
                evenCount += 1
            n = n >> 2

        return self.isMultipleOfThree(abs(oddCount - evenCount))




# Driver Code


s = "011"

print("Type Casting Solution")
ob = Solution()
ans = ob.isDivisible(s)
print(ans)

print("Bit Manipulation Solution")
obj = BitManSolution()
newAns = ob.isDivisible(s)
print(newAns)