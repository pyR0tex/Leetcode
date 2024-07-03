# given a linked list, return it reversed
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
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


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # approach1: iterative
        # basically swap every value and iterate prev
        # prev should end at the last value
        cur, prev = head, None
        while cur:
            n = cur.next
            cur.next = prev
            prev = cur
            cur = n
            # another solution:
            #cur.next, prev, cur = prev, cur, cur.next
        return prev

    def reverseList1(self, head: ListNode) -> ListNode:
        # approach2: recursive
        return self.recursiveReverse(head)

    def recursiveReverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self.recursiveReverse(n, node)

def main():
    S = Solution()
    L = LinkedList()
    L1 = LinkedList()
    rList = LinkedList()
    rList1 = LinkedList()

    for i in range(5):
        L.insert(i+1)
        L1.insert(i+1)

    L.printList()
    rList.head = S.reverseList(L.head)
    rList.printList()

    L1.printList()
    rList1.head = S.reverseList1(L1.head)
    rList1.printList()

if __name__ == "__main__":
    main()
