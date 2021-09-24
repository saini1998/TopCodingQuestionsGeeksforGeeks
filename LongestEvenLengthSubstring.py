"""

For given string ‘str’ of digits, find length of the longest substring of ‘str’, such that the length of the substring is 2k digits and sum of left k digits is equal to the sum of right k digits.
 

Input:

The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows.
Each test case contains a string string of length N.

Output:

Print length of the longest substring of length 2k such that sum of left k elements is equal to right k elements and if there is no such substring print 0.


Constraints:

1 ≤ T ≤ 100
1 ≤ N ≤ 100

Example:

Input:
2
000000
1234123

Output:
6
4  

"""

# Time Complexity: O(n^2)
# Space Complexity: O(1)

def findLength(str):
    n = len(str)
    total = [0] * (n+1)
    
    for i in range(1, n + 1):
        total[i] = (total[i - 1] + int(str[i - 1]) - int('0'))
 
    ans = 0 
    print("total:",end=' ')
    print(total)
    l = 2
    while(l <= n):
        print("l before loop:", end=' ')
        print(l)
        print("Loop range: 0", end=' ')
        print(n-l)
        for i in range(n - l + 1):
            print("i:", end=' ')
            print(i)
            a = total[i + l //2] -total[i]
            b = total[i + l] -total[i + l // 2]
            print("Check whether a: ", total[i + l //2], " - ",total[i], " = ",a, " == b: ",total[i + l]," - ",total[i + l // 2], " = ", b)
            if (total[i + l // 2] -total[i] == total[i + l] -total[i + l // 2]):
                ans = max(ans, l)
                print("ans:", end=' ')
                print(ans)
                
        l = l + 2
        print("l after loop:", end=' ')
        print(l)
    print("ans:", end=' ')
    print(ans)
     
    return ans
    

    
if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        
        print(findLength(s))