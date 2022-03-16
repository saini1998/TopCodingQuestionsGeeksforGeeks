



def intersectWithDup(list1, list2):

    rev1 = sorted(list1, reverse=True)
    rev2 = sorted(list2, reverse=True)

    i, j = 0, 0

    res = []

    while i < len(rev1) or j < len(rev2):
        if rev1[i] == rev2[j] :
            k = rev1.pop(i)
            res.append(k)
            rev2.pop(j)
            i = i - 1
            j = j - 1

            if i == len(rev1):
                j = j+1
            if j == len(rev2):
                i = i+1
            else:
                i = i + 1
                j = j + 1

        elif rev1[i] > rev2[j]:
            if i == len(rev1):
                j = j+1
            if j == len(rev2):
                i = i+1
            else:
                i = i + 1

        elif rev2[j] > rev1[i]:
            if i == len(rev1):
                j = j+1
            if j == len(rev2):
                i = i+1
            else:
                j = j + 1
        
    return res
        
        


from collections import Counter
    # a = Counter(list1)
    # b = Counter(list2)
    # set1 = set(list1)
    # set2 = set(list2)
    # list3 = list(set1 & set2)
    # list4 = []
    # for i in list3:
    #     list4.extend([i]*min(a[i], b[i]))

    # ans = sorted(list4, reverse=True)
    # return ans


list1 = [7,7,5,1,4]
list2 = [6,4,4,3,1]

ans = intersectWithDup(list1,list2)
print(ans)



"""

Question.

    7   7   5   1   4
    6   4   4   3   1

One match of 4 and one match of 1.
Answer is [4, 1] in descending order.

"""