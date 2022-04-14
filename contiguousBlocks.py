
s = 'aabbbaabbaaaabb'
l = ['']

for i,c in enumerate(s):
    if c in l[-1]:
        cc = l[-1]
        cn = cc+c
        l[-1] = cn
    else:
        l.append(c)

l.pop(0)
print(l)
lt = []

for item in l:
    lt.append(len(item))

sum = 0
m = max(lt)

for i in lt:
    sum += (m-i)
    print("sum = ", sum)
    

print(sum)
    

