# given 2 linked lists, merge them together and return the head

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # approach
        # Good stuff, approved on leetcode
        # make head and temp node and point temp to head
        # loop through both lists and point temp.next to smaller number
        # once either are null, loop through not-NUll list to the linked list
        # return head.next(official head)
        head = ListNode()
        temp = head
        while(list1 and list2):
            print(list1.val,list2.val)
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        if list1:
            temp.next = list1
        if list2:
            temp.next = list2
        return head.next
def main():
    S = Solution()
    # list1
    m1 = ListNode(1)
    m2 = ListNode(2)
    m3 = ListNode(4)
    m1.next = m2
    m2.next = m3
    # list2
    n1 = ListNode(1)
    n2 = ListNode(3)
    n3 = ListNode(4)
    n1.next = n2
    n2.next = n3

    flag = S.mergeTwoLists(m1,n1); print(flag.val)

if __name__ == '__main__':
    main()
