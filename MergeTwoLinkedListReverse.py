"""

Given two linked lists of size N and M, which are sorted in non-decreasing order. The task is to merge them in such a way that the resulting list is in decreasing order.

Input:
First line of input contains number of testcases T. For each testcase, first line of input conatains length of both linked lists N and M respectively. Next two lines contains N and M elements of two linked lists.

Output:
For each testcase, print the merged linked list which is in non-increasing order.

User Task:
The task is to complete the function mergeResult() which takes reference to the heads of both linked list and returns the pointer to the merged linked list.

Constraints:
1 <=T<= 50
1 <= N, M <= 1000

Example:
Input:
2
4 3
5 10 15 40 
2 3 20
2 2
1 1
2 4

Output:
40 20 15 10 5 3 2
4 2 1 1 

Explanation:
Testcase 1: After merging the two lists in decreasing order, we have new lists as 40->20->15->10->5->3->2.

"""

def mergeResult(a,b):
    if (a == None) and (b == None):
        return None

    result = None
    
    while (a != None) and (b != None):
        if (a.data <= b.data):
            temp = a.next
            a.next = result
            result = a
            a = temp

        else:
            temp = b.next
            b.next = result
            result = b
            b = temp

    while (a != None):
        temp = a.next
        a.next = result
        result = a
        a = temp

    while (b != None):
        temp = b.next
        b.next = result
        result = b
        b = temp
    
    return result

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
        else:
            newNode = Node(val)
            self.tail.next = newNode
            self.tail = self.tail.next

def printList(head):
    temp = head
    while temp:
        print(temp.data, end=' ')
        temp = temp.next
    print()

if __name__ == '__main__':
    for t in range(int(input())):
        n1, n2 = [int(x) for x in input().split()]

        arr1 = [int(x) for x in input().split()]
        llist1 = LinkedList()
        for i in arr1:
            llist1.insert(i)

        arr2 = [int(x) for x in input().split()]
        llist2 = LinkedList()
        for i in arr2:
            llist2.insert(i)

        resultHead = mergeResult(llist1.head, llist2.head)
        printList(resultHead)