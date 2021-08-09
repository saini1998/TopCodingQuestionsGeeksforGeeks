"""

A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.

Given three integers a, b and c, return any string s, which satisfies following conditions:

s is happy and longest possible.
s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.
s will only contain 'a', 'b' and 'c' letters.
If there is no such string s return the empty string "".

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 2, b = 2, c = 1
Output: "aabbc"
Example 3:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It's the only correct answer in this case.
 

Constraints:

0 <= a, b, c <= 100
a + b + c > 0

"""

# Time Complexity = O(log N)

import heapq

class Solution:
    def longestDiverseString(self, A, B, C):

        result = ''
        while A > 0 or B > 0 or C > 0:
            arr = []
            if A and (len(result) < 2 or result[-1] != 'a' or result[-2] != 'a'):
                heapq.heappush(arr, (-A, 'a'))
            if B and (len(result) < 2 or result[-1] != 'b' or result[-2] != 'b'):
                heapq.heappush(arr, (-B, 'b'))
            if C and (len(result) < 2 or result[-1] != 'c' or result[-2] != 'c'):
                heapq.heappush(arr, (-C, 'c'))
            if not arr:
                break            
            result += arr[0][1]
            A -= arr[0][1] == 'a'
            B -= arr[0][1] == 'b'
            C -= arr[0][1] == 'c'           

        return result


a, b, c = 7, 1, 0

print(Solution().longestDiverseString(a,b,c))

