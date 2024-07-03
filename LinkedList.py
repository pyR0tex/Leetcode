# LinkedList implementation

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    # insert
    def insert(self, val: int) -> None:
        node = ListNode(val)
        if not self.head:
            self.head = node
            return
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = node

    # printList
    def printList(self):
        node = self.head
        lList = []
        while(node):
            lList.append(node.val)
            node = node.next
        print(lList)
