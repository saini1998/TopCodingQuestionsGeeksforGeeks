def solution(a, b):
    sum = []
    count = 0

    i = 0
    while i<len(a):
        s = a[i] + b[i]
        sum.append(s)

        count += 1
        i += 1
    
    j = 0
    while j< (len(sum)-1):
        if sum[j] == sum[j+1]:
            count += 1

        j += 1
    
    print(sum)
    return count

A = [2, -2, 5, 3]
B = [1,5,-1,1]

print(solution(A,B))
