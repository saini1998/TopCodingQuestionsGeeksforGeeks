def solution(x):
    # Your code here
    ans = ""
    for e in x:
        if e >= 'a' and e <= 'z':
            ans += chr(ord('a') + (ord('z') - ord(e)))
        else:
            ans += e

    
    print(ans)

a = "Yvzs! I xzm'g"

solution(a)