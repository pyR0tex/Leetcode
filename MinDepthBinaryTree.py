# 111. Minimum Depth of Binary Tree

from BinarySearchTree import Node
from BinarySearchTree import BinarySearchTree as BST

def minDepth(root) -> int:
    print("min depth of binary tree")


if __name__ == '__main__':
    bst = BST()
    values = [3,9,20,15,7]
    root = None
    for v in values:
        root = bst.insert(root, v)
    bst.inOrderBST()