# remove Nth node from the end of list
from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    # insert
    def insert(self, val : int):
        node = ListNode(val)
        if(self.head):
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = node
        else:
            self.head = node

    def printList(self):
        temp = self.head
        lList = []
        while(temp):
            lList.append(temp.val)
            temp = temp.next
        # print(lList)
        return lList

def removeNthFromEnd(head : Optional[ListNode], n : int) -> Optional[ListNode]:
    temp = ListNode(0, head)
    left, right = temp, head
    for _ in range(n):
        right = right.next
    while right:
        left = left.next
        right = right.next
    left.next = left.next.next
    return temp.next

def main():
    lList, n = LinkedList(), 4
    for counter in range(5):
        lList.insert(counter + 1)
    print("inputList:",lList.printList(),"n =",n)

    rList = LinkedList()
    rList.head = removeNthFromEnd(lList.head, n)
    print(rList.printList())

if __name__ == '__main__':
    main()
