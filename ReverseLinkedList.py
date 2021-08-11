"""

Given a linked list of N nodes. The task is to reverse this list.

Example 1:

Input:
LinkedList: 1->2->3->4->5->6
Output: 6 5 4 3 2 1
Explanation: After reversing the list, 
elements are 6->5->4->3->2->1.
Example 2:

Input:
LinkedList: 2->7->8->9->10
Output: 10 9 8 7 2
Explanation: After reversing the list,
elements are 10->9->8->7->2.
Your Task:
The task is to complete the function reverseList() with head reference as the only argument and should return new head after reversing the list.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 104

"""

class Solution:
    def reverseListWithThreePointers(self, head):
        later = None
        prev = None
        curr = head
        
        while (curr != None) :
            later = curr.next
            curr.next = prev
            prev = curr
            curr = later
        
        head = prev
        return head

    def reverseListWithTwoPointers(self, head):
        curr = head
        later = None

        while (curr.next != None):
            later = curr.next
            curr.next = later.next
            later.next = head
            head = later

        return head

    def reverseListUsingStack(self, head):
        stack, temp = [], head
        while temp:
            stack.append(temp)
            temp = temp.next

        head = temp = stack.pop()

        while len(stack) > 0:
            element = stack.pop()
            temp.next = element
            temp = element

        element.next = None
        return head

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

lis2 = LinkedList()
lis2.insert(2)
lis2.insert(7)
lis2.insert(8)
lis2.insert(9)
lis2.insert(10)

lis3 = LinkedList()
lis3.insert(2)
lis3.insert(7)
lis3.insert(8)
lis3.insert(9)
lis3.insert(10)

head1 = Solution().reverseListWithThreePointers(lis.head)
print("After Reverse With Three pointers")
printList(head1)

head2 = Solution().reverseListWithTwoPointers(lis2.head)
print("After Reverse With Two pointers")
printList(head2)

head3 = Solution().reverseListUsingStack(lis3.head)
print("After Reverse With Stack")
printList(head3)

