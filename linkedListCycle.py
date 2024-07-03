# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        d = {}
        while(head):
            if head in d.keys():
                return True
            else:
                d[head] = True
            head = head.next
        return False

def main():
    S = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2
    n3 = ListNode(3)
    n2.next = n3
    n4 = ListNode(4)
    n3.next = n4
    n5 = ListNode(5)
    n4.next = n5
    n6 = ListNode(6)
    n5.next = n6
    n6.next = n2

    flag = S.hasCycle(n1); print(flag)

if __name__ == '__main__':
    main()
