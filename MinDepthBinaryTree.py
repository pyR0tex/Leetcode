# 111. Minimum Depth of Binary Tree

from BinarySearchTree import BinaryTree

def minDepth(root) -> int:
    print("min depth of a binary tree")

    def _depthHelper(node):
        if node.left and node.right:
            return min(1+_depthHelper(node.left), 1+_depthHelper(node.right))
        elif node.left:
            return 1+_depthHelper(node.left)
        elif node.right:
            return 1+_depthHelper(node.right)
        else:
            return 1
    if root:
        depth = _depthHelper(root)
    else:
        depth = 0
    return depth

if __name__ == '__main__':
    tree = BinaryTree()
    nodes = [3,9,20,None,None,15,7]
    root = tree.CreateTree_LeetCode(nodes)
    tree.printTree()

    minD = minDepth(root)
    print(f"minimum depth of tree: {minD}, should retun 2")

    tree1 = BinaryTree()
    nodes = [2,None,3,None,4,None,5,None,6]
    root1 = tree1.CreateTree_LeetCode(nodes)
    tree1.printTree()

    minD = minDepth(root1)
    print(f"minimum depth of tree: {minD}, should return 5")