# 109 Sorted Array to Binary Search tree
from typing import Optional
from BinarySearchTree import Node

def sortedArrayToBST(nums: list[int]) -> Optional[Node]:
    print("Convert Sorted Array to Binary Search Tree")
    
    if len(nums) is 0:
        return None
    return solve(nums, 0, len(nums) - 1)


def solve(nums: list[int], left: int, right: int) -> Optional[Node]:
    if(left > right):
        return None
    mid = (left + right) //2
    node = Node(nums[mid])
    node.left = solve(nums, left, mid-1)
    node.right = solve(nums, mid+1, right)
    
    return node
    
if __name__ == '__main__':

    nums = [-10,-3,0,5,9]
    bst = [-10,-3,0,5,9]

    print("Input:", end=" ")
    print([val for val in nums], end=" ")
    print("---> BST:" , end=" ")
    print([val for val in bst])
