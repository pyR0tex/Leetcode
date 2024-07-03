# given a ListNode head and val, remove all nodes with the val from list, return head
import LinkedList as L # import local linked list file

##### TEST VALUES   #####################
# test 1
lList = L.LinkedList()
for i in range(7):
    lList.insert(i+1)
lList.printList()
val = 6; print('remove val:',val)
#########################################


class Solution:
    def removeElements(self, head: L.ListNode, val: int)->L.ListNode:
        print('removeElements')
        # approach:
        # list of edge cases to consider:
        # (1)   The linked list is empty, i.e. the head node is None.
        # (2)   Multiple nodes with the target value in a row.
        # (3)   The head node has the target value.
        # (4)   The head node, and any number of nodes immediately after it have the target value.
        # (5)   All of the nodes have the target value.
        # (6)   The last node has the target value.

        rHead = L.ListNode()
        rHead.next = head
        node = rHead
        while(node.next):
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return rHead.next


def main():
    S = Solution()
    # function call
    r = S.removeElements(lList.head, val)
    # print new list
    rList = L.LinkedList()
    rList.head = r
    rList.printList()

if __name__ == '__main__':
    main()
