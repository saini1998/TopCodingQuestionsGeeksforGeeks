"""

A binary heap is a Binary Tree with the following properties:
1) Its a complete tree (All levels are completely filled except possibly the last level and the last level has all keys as left as possible). This property of Binary Heap makes them suitable to be stored in an array.

2) A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, the key at the root must be minimum among all keys present in Binary Heap. The same property must be recursively true for all nodes in Binary Tree. Max Binary Heap is similar to MinHeap.

You are given an empty Binary Min Heap and some queries and your task is to implement the three methods insertKey,  deleteKey,  and extractMin on the Binary Min Heap and call them as per the query given below:
1) 1  x  (a query of this type means to insert an element in the min-heap with value x )
2) 2  x  (a query of this type means to remove an element at position x from the min-heap)
3) 3  (a query like this removes the min element from the min-heap and prints it ).

Example 1:

Input:
Q = 7
Queries:
insertKey(4)
insertKey(2)
extractMin()
insertKey(6)
deleteKey(0)
extractMin()
extractMin()
Output: 2 6 - 1
Explanation: In the first test case for
query 
insertKey(4) the heap will have  {4}  
insertKey(2) the heap will be {2 4}
extractMin() removes min element from 
             heap ie 2 and prints it
             now heap is {4} 
insertKey(6) inserts 6 to heap now heap
             is {4 6}
deleteKey(0) delete element at position 0
             of the heap,now heap is {6}
extractMin() remove min element from heap
             ie 6 and prints it  now the
             heap is empty
extractMin() since the heap is empty thus
             no min element exist so -1
             is printed.
Example 2:

Input:
Q = 5
Queries:
insertKey(8)
insertKey(9)
deleteKey(1)
extractMin()
extractMin()
Output: 8 -1
Your Task:
You are required to complete the 3 methods insertKey() which take one argument the value to be inserted, deleteKey() which takes one argument the position from where the element is to be deleted and extractMin() which returns the minimum element in the heap(-1 if the heap is empty)

Expected Time Complexity: O(Q*Log(size of Heap) ).
Expected Auxiliary Space: O(1).

Constraints:
1 <= Q <= 104
1 <= x <= 104

"""
from heapq import *

def insertKey(x):
    heapIsDefault = True
    for h in heap:
        if h != 0:
            heapIsDefault = False
            break
    if heapIsDefault:
        heap.clear()
            
    heappush(heap, x)
    return

def parent(i):
    return (i-1)//2

def decreaseKey(i, newValue):
    heap[i] = newValue
    while ( i != 0 and heap[parent(i)] > heap[i] ):
        heap[parent(i)], heap[i] = heap[i], heap[parent(i)]
    return

def deleteKey(i):
    if i >= len(heap):
        return -1
    decreaseKey(i, -1)
    extractMin()
    return
    
def extractMin():
    heapEmpty = True
    for h in heap:
        if h != 0:
            heapEmpty = False
            break
    if heapEmpty:
        return -1
    top = heappop(heap)
    return top

def getMin():
    return heap[0]

# global
heap = []
currSize = 0

if __name__ == "__main__":
    t = int(input("enter number of test cases: "))
    while t:
        n = int(input("enter number of queries: "))
        a = list(map( int, input("enter queries with spaces: ").strip().split() ))

        curSize = 0
        heap = [0 for i in range(n)]

        # print("querries as list: ", a)
        # print("heap at start: ", heap)

        i = 0
        while i<len(a):
            if a[i] == 1:
                insertKey(a[i+1])
                i += 1
            elif a[i] == 2:
                deleteKey(a[i+1])
                i += 1
            else:
                print(extractMin(), end = " ")
            i += 1
        
        print()
        t -= 1