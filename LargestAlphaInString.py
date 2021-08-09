"""
Given a string str, our task is to find the Largest Alphabetic Character, whose both uppercase and lowercase are present in the string. The uppercase character should be returned. If there is no such character then return -1 otherwise print the uppercase letter of the character.

Examples: 

Input: str = “admeDCAB” 
Output: D 
Explanation: 
Both the uppercase and lowercase characters for letter D is present in the string and it is also the largest alphabetical character, hence our output is D.

Input: str = “dAeB” 
Output: -1 
Explanation: 
Althogh the largest character is d in the string but the uppercase version is not present hence the output is -1. 

"""
"""
            Time complexity: O(n) where n is length of string. 
            Space complexity: O(52)
"""

class Solution:
    def largestCharacter(self, S):
        upperCase = [False] * 26
        lowerCase = [False] * 26
        arrayS = list(S)
        for i in range(len(arrayS)):
            if arrayS[i].islower():
                lowerCase[ord(arrayS[i]) - ord('a')] = True
            if arrayS[i].isupper():
                upperCase[ord(arrayS[i]) - ord('A')] = True
        
        for i in range(25,-1,-1):
            if (upperCase[i] and lowerCase[i]):
                return chr(i + ord('A'))
        
        return "NO"


S1 = "Codility"
S2 = "WeTestCodErs"

print("Largest Character for 'Codility': " + Solution().largestCharacter(S1))
print("Largest Character for 'WeTestCodErs': " + Solution().largestCharacter(S2))