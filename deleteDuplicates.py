# given a linked list, remove all duplicate elements and return head

from LinkedList import ListNode, LinkedList

#######  TEST CASES  #########################################
lList = LinkedList()
d = [1,1,2,3,4,5,6,6,6,6,7,7]
d1 = [0,0,0,0,0,0,0]
for i in d:
    lList.insert(i)
############################################

class Solution:
    def deleteDuplicates(self, head:ListNode) -> ListNode:
        # approach:
        # declare iterable node from head
        # while loop: check if node and node.next exist
        # constraints: check if next.val == current val: node.next = node.next.next
        # contsraints: if next.val is different, then just iterate to next node
        node = head
        while node and node.next:
            if node.next.val == node.val:
                node.next = node.next.next
            else:
                node = node.next
        # approach 2
        # both perform around the same
        # the difference is approach 2 uses a second while loop to just skip ->
        #  -> all the val == next.val
        # while node:
        #     while node.next and node.next.val == node.val:
        #         node.next = node.next.next
        #     node = node.next
        return head


def main():
    S = Solution()
    rList = LinkedList()
    # function call
    rList.head = S.deleteDuplicates(lList.head)
    rList.printList()

if __name__ == '__main__':
    main()
