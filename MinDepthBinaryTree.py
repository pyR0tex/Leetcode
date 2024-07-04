# 111. Minimum Depth of Binary Tree

from BinarySearchTree import BinaryTree

def minDepth(root) -> int:
    print("min depth of binary tree")


if __name__ == '__main__':
    tree = BinaryTree()
    nodes = [3,9,20,None,None,15,7]
    root = tree.CreateTree_LeetCode(nodes)
    tree.printTree()