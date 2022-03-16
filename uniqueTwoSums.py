


def uniqueTwoSum(nums, target):
  ans, comp = set(), set()
  for n in nums:
    c = target-n
    if c in comp:
      res = (n, c) if n > c else (c, n)
      if res not in ans:
        ans.add(res)
    comp.add(n)
  return len(ans)

# Driver Code
arr = [ 5,7,9,13,11,6,6,3,3 ]
N = len(arr)
K = 12

ans = uniqueTwoSum(arr,K)
print(ans)


"""

Question.

5+7
3+9
6+6

12

"""