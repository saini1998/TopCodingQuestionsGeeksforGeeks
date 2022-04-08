"""

Given K sorted linked lists of different sizes. The task is to merge them in such a way that after merging they will be a single sorted linked list.

Example 1:

Input:
K = 4
value = {{1,2,3},{4 5},{5 6},{7,8}}
Output: 1 2 3 4 5 5 6 7 8
Explanation:
The test case has 4 sorted linked 
list of size 3, 2, 2, 2
1st    list     1 -> 2-> 3
2nd   list      4->5
3rd    list      5->6
4th    list      7->8
The merged list will be
1->2->3->4->5->5->6->7->8.
Example 2:

Input:
K = 3
value = {{1,3},{4,5,6},{8}}
Output: 1 3 4 5 6 8
Explanation:
The test case has 3 sorted linked
list of size 2, 3, 1.
1st list 1 -> 3
2nd list 4 -> 5 -> 6
3rd list 8
The merged list will be
1->3->4->5->6->8.
Your Task:
The task is to complete the function mergeKList() which merges the K given lists into a sorted one. The printing is done automatically by the driver code.

Expected Time Complexity: O(nk Logk)
Expected Auxiliary Space: O(k)
Note: n is the maximum size of all the k link list

Constraints
1 <= K <= 103

"""

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, x):
        if self.head == None:
            self.head = Node(x)
            self.tail = self.head

        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next
    
    def print(self):
        top = self.head
        while top:
            print(top.data, end=" ")
            top = top.next
        print()

import heapq as hq

class Solution:
    def mergeKLists(self, arr, k):
        heap = []
        for head in arr:
            top = head
            while top:
                hq.heappush(heap, top.data)
                top = top.next

        print(heap)

        mergedLL = LinkedList()
        n = len(heap)
        for i in range(0,n):
            mergedLL.add(hq.heappop(heap))

        return mergedLL.head



if __name__ == "__main__":
    list1 = LinkedList()
    for i in range(1, 4):
        list1.add(i)

    list2 = LinkedList()
    for i in range(4, 7):
        list2.add(i)

    list3 = LinkedList()
    for i in range(5, 7):
        list3.add(i)
    
    list4 = LinkedList()
    for i in range(7, 9):
        list4.add(i)

    list1.print()
    list2.print()
    list3.print()
    list4.print()

    heads = []

    heads.append(list1.head)
    heads.append(list2.head)
    heads.append(list3.head)
    heads.append(list4.head)

    for i in range(4):
        print(heads[i].data, end=" ")
    print()

    k = 4

    finalHead = Solution().mergeKLists(heads,k)
    while finalHead:
        print(finalHead.data,end= " ")
        finalHead = finalHead.next
    print()
