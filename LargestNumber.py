"""

Given a list of non-negative integers nums, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
Example 3:

Input: nums = [1]
Output: "1"
Example 4:

Input: nums = [10]
Output: "10"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109

"""


def largestNumber(nums) :
    nums = sorted(nums,key=lambda x:x / (10 ** len(str(x)) - 1 ), reverse=True)
    str_nums = [str(num) for num in nums]
    res = ''.join(str_nums)
    # res = str(int(res))
    return res


nums = [3,30,34,5,9]

print(largestNumber(nums))