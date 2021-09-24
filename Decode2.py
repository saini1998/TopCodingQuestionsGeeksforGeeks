def count(s):
    lt = [char for char in s]
    twoD = []
    oneD = []
    print('lt: ', lt)

    stD = {}

    i = 0
    while(i<len(lt)):
        if i+2 < len(lt):
            if lt[i+2] == '#':
                st = ""
                st = st + lt[i]
                st = st + lt[i+1]
                stD[st] = 1
                twoD.append(st)
                i += 2
            else:
                if lt[i] != "#":
                    stD[lt[i]] = 1
                    oneD.append(lt[i])
                i += 1
        else:
            i += 1

    print("stD ",stD)
    print("twoD ", twoD)
    print("oneD ", oneD)

    iTwoD = [int(i) for i in twoD]
    iOneD = [int(i) for i in oneD]
    
    ans = [0] * 26

    for i in iTwoD:
        if ans[i-1] == 0:
            ans[i-1] = 1
        else:
            ans[i-1] += 1

    for i in iOneD:
        if ans[i-1] == 0:
            ans[i-1] = 1
        else:
            ans[i-1] += 1

    print(ans)


st = "1226#24#"

st1 = "2110#(2)"

count(st1)