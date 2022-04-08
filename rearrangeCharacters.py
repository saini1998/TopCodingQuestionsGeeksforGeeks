"""

Given a string S with repeated characters (only lowercase). The task is to rearrange characters in a
string such that no two adjacent characters are same.
Note: It may be assumed that the string has only lowercase English alphabets.
Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases
follow. Each test case contains a single line containing a string of lowercase english alphabets.
Output:
For each test case in a new line print "1" (without quotes) if the generated string doesn't contains
any same adjacent characters, else if no such string is possible to be made print "O" (without
quotes).
Constraints:
1 <=T<=100
1<= length of string <= 104
Example:

Input:
3
geeksforgeeks
bbbabaaacd
bbbbb

Output:
1
1
0

Explanation:
Testcase 1: All the repeated characters of the given string can be rearranged so that no adjacent
characters in the string is equal.
Testcase 3: Repeated characters in the string cannot be rearranged such that there should not be
any adjacent repeated character.

"""

from heapq import *

def solution(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    
    heap = [(-v,k) for k,v in freq.items()]
    heapify(heap)
    ans = []

    while len(heap) > 1:
        x = heappop(heap)
        y = heappop(heap)
        ans.extend([x[1], y[1]])
        if x[0] < -1:
            heappush(heap, (x[0]+1, x[1]))
        if y[0] < -1:
            heappush(heap, (y[0]+1, y[1]))

    if heap:
        if heap[0][0] < -1:
            return 0
        ans.append(heap[0][1])

    # return "".join(ans)
    return 1

if __name__ == "__main__":
    T = int(input())
    while T>0:
        line = input()
        ans = solution(line)
        print(ans)
        T -= 1