class Solution:

    def reverse(self, head, k):
        if head == None:
          return None
        current = head
        later = None
        prev = None
        count = 0
 
        while(current is not None and count < k):
            later = current.next
            current.next = prev
            prev = current
            current = later
            count += 1

        if later is not None:
            head.next = self.reverse(later, k)
 
        return prev

class Node:
    def __init__(self, val):
        self.data = val
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


lis = LinkedList()
lis.insert(2)
lis.insert(7)
lis.insert(8)
lis.insert(9)
lis.insert(10)

printList(lis.head)

k = 3

head = Solution().reverse(lis.head, k)
print("After Reverse With Stack")
printList(head)

