"""

Alex has a list of Items to purchase at a market. The owner offers to
discount each Item after the first one by the lowest marked price
among the prior Items. No Item's price can be discounted below 0,
and the list of Items may not be reordered. Calculate the payable
amount.

Example
prices = [2, 5, 1, 41

Alex pays 2 for the first Item since there are no previous Items to
compare to.
The second Item costs 5 - 2=3.
The third Item Is free: max(1 - min(2, 5), 0) = max(-1, 0) = 0.
The fourth Item costs 4 - 1
=3,

The total cost to purchase all Items Is 2 + 3 + 0 + 3 = 8.
The first Item is never discounted and the minlmum cost of any Item is 0.

Function Description
Complete the function calculateAmount In the editor below. The
function must return Alex's total cost to purchase all the Items.

calculateAmount has the following parameter(s).
int prices[n]: the orlginal prices of each of the Items selected
int: the total cost to purchase the Items after any discounts are applied

Constraints
1 <= n <= 10^5
1 <= prices[i] <= 10^7, where 0<=i<=n

"""

def solution(a):
    da = []
    da.append(a[0])
    discount = a[0]
    for i in range(1,len(a)):
        discount = min(discount, a[i])
        value = a[i] - discount
        if value >= 0:
            da.append(value)
        else:
            da.append(a[i])
    total = sum(da)
    return total


arr = [2,5,1,4]

res = solution(arr)
print(res)