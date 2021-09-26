
def solution(s, names):
    noOfCounts = {}

    for name in names:
        counts = {}
        for l in name:
            counts[l] = s.count(l) // name.count(l)
        
        noOfCounts[min(list(counts.values()))] = name
    
    print(noOfCounts)

    return noOfCounts[max(list(noOfCounts.keys()))]

    

s = 'billobillollobbi'
names = ['bill', 'bob']
print(solution(s, names))