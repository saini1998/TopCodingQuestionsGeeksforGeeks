a= [5,3,2,1,3]
o = [[0,1], [1,3]]

def performOperations(a, o):
    for start,end in o:
        print("start: ",start," end: ",end)
        if start > 0:
            a[start:end+1] = a[end:start-1:-1]
        else:
            a[start:end + 1] = a[end::-1]
            print("a: ",a)


performOperations(a,o)

print(a)

"""
Question.

reverse an array with another array that has start and end indexes.

5   3   2   1   3

|
v

[0,1]

|
v

3   5   2   1   3

|
v

[1,3]

|
v

3   1   2   5   3

"""