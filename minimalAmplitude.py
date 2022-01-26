def solution(a, k):
    newA = a + a
    n = len(a)
    res = 999999
    start = k
    while start<=n:
        m = n - k
        mn = 999999
        mx = -99999
        for j in range(0,m):
            idx = start + j
            mn = min(mn, newA[idx])
            mx = max(mx, newA[idx])
        
        res = min(res, mx-mn)
        start += 1
    
    print(res)


a = [8,8,4,3]
a1 = [5,3,6,1,3]
a3 = [3,5,1,3,9,8]
k = 4

solution(a3,k)