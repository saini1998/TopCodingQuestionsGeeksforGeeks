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

"""
Question.

Decode the string. 
Leave punctuations and capital letters as it is. 
Encoding is done for small letters only. So a->z, b->y, c->x,...,y->b,z->a.

"""