# return the middle node of a singly linked list
from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    # insert
    def insert(self, val):
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
        print(lList)

def middleNode(head : Optional[ListNode]) -> Optional[ListNode]:
    slow, fast = head, head

    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
    return slow

def main():
    lList = LinkedList()
    for counter in range(10):
        lList.insert(counter + 1)
    rList = LinkedList()
    rList.head = middleNode(lList.head)
    rList.printList()

if __name__ == '__main__':
    main()
