# 144. Binary Tree Preorder Traversal

from BinarySearchTree import BinaryTree

def PreOrderTraversal(root) -> list[int]:    
    preOrderList = []
    def _helperPreOrder(root):
        if root:
            preOrderList.append(root.val)
            _helperPreOrder(root.left)
            _helperPreOrder(root.right)

    _helperPreOrder(root)
    return preOrderList


if __name__ == '__main__':
    tree1 = BinaryTree()
    Nodes = [1, None, 2, 3]
    root = tree1.CreateTree_LeetCode(Nodes)
    tree1.printTree()
    preOrder = PreOrderTraversal(root)
    print(f"PreOrder: {[p for p in preOrder]}")