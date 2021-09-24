"""

Given two lists V1 and V2 of sizes n and m respectively. Return the list of elements common to both the lists and return the list in sorted order. Duplicates may be there in the output list.

Example:

Input:
n = 5
v1[] = {3, 4, 2, 2, 4}
m = 4
v2[] = {3, 2, 2, 7}
Output:
2 2 3
Explanation:
The common elements in sorted order are {2 2 3}
Your Task:
This is a function problem. You need to complete the function common_element that takes both the lists as parameters and returns a list of common elements.

Constraints:
1 ≤ n, m ≤ 105
1 ≤ Vi ≤ 105

"""

class Solution:
    def common_element(self,v1,v2):
        com_ele={}
        for i in v1:
            if i in com_ele:
                com_ele[i]+=1
            else:
                com_ele[i]=1
        result=[]
        for i in v2:
            if i in com_ele:
                if com_ele[i]>0:
                    com_ele[i]-=1
                    result.append(i)
        return sorted(result)

v1 = [3, 4, 2, 2, 4]
v2 = [3, 2, 2, 7]
print(Solution().common_element(v1, v2))
