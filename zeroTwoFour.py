

def countNumbers(n):
    intL = list(range(0, n+1))
    strL = [str(x) for x in intL]
    count = {
        "z" : 0,
        "t" : 0, 
        "f" : 0
    }
    for i in strL:
        for j in range(0,len(i)):
            if i[j] == "0":
                count["z"] += 1
            if i[j] == "2":
                count["t"] += 1
            if i[j] == "4":
                count["f"] += 1
                
    return count["z"] + count["t"] + count["f"]


N = 22

print(list(range(0,23)))

print(countNumbers(N))

