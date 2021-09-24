def count(s):
    if s == '':
        return [0] * 26

    lt = [char for char in s]
    ltCopy = [char for char in s]
    
    sb = {}

    print('lt: ', lt)
    j = 0
    while (j<len(lt)):
        if j+2<len(lt):
            if lt[j] == '(':
                t = j
                lt.pop(j)
                lt.pop(j+1)
                if lt[j-1] == '#':
                    temp = '' + lt[j-3] + lt[j-2]
                    if temp in sb:
                        sb[temp] += int(lt[j])
                    else: 
                        sb[temp] = int(lt[j])
                else:
                    temp = '' + lt[j-1]
                    if temp in sb:
                        sb[temp] += int(lt[j])
                    else: 
                        sb[temp] = int(lt[j])
                    # sb[temp] = int(lt[j])
                lt.pop(j)
                j = t
            else:
                j += 1
        else:
            j += 1

    print('sb: ', sb)
    print('new lt: ', lt)

    stD = {}

    i = 0
    while(i<len(lt)):
        if i+2 < len(lt):
            if lt[i+2] == '#':
                st = ""
                st = st + lt[i]
                st = st + lt[i+1]
                stD[st] = 1
                i += 3
            else:
                if lt[i] != "#":
                    stD[lt[i]] = 1
                i += 1
        else:
            stD[lt[i]] = 1
            i += 1

    print("stD ",stD)

    k = 0
    while (k<len(ltCopy)):
        if k+2<len(ltCopy):
            if ltCopy[k] == '(':
                if ltCopy[k-1] != '#':
                    stD[ltCopy[k-1]] = ltCopy[k+1]
                    k += 3
                elif ltCopy[k-1] == '#':
                    x = ""
                    x = x + ltCopy[k-3]
                    x = x + ltCopy[k-2]
                    stD[x] = ltCopy[k+1]
                    k += 3
                
            else:
                k += 1
        else:
            k += 1

    print("new stD ",stD)
    
    ans = [0] * 26

    for key, value in stD.items():
        if key in sb:
            ans[idx-1] = int(sb[key])
        else:
            idx = int(key)
            ans[idx-1] = int(value)

    print(s, " : ", ans)
    print()


st = "1226#24#"
st1 = "2(3)110#(2)"
st2 = "1(2)23(3)"
st4 = "23#(2)24#25#26#23#(3)"
# st4 = 

count(st4)

# print(count(''))
# count(st)
# count(st1)
# count(st2)
# count(st3)