# Binary Search Tree Implementation
import collections

class Node:
    def __init__(self, val=0):
        self.left = None
        self.right = None
        self.val = val

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def getRoot(self) -> Node:
        if self.root:
            return self.root
        return None

    def insert(self, root, val) -> Node:
        # if the tree is empty
        if root is None:
            root = Node(val)
            self.root = root
            return root
        
        # recursion down the binary tree
        if val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)

        return root
    
    def printTree(self):
        def _print_tree(node, level=0):
            if node:
                _print_tree(node.right, level + 1)
                print('   ' * level + str(node.val))
                _print_tree(node.left, level + 1)
        _print_tree(self.root)

    def inOrderBST(self):
        def _inOrderBST_Helper(node):
            rList = []
            if node:
                rList += _inOrderBST_Helper(node.left)
                rList.append(node.val)
                rList += _inOrderBST_Helper(node.right)
            return rList
        return _inOrderBST_Helper(self.root)
    
    def preOrderBST(self):
        def _preOrderBST_Helper(root):
            rList = []
            if root:
                rList.append(root.val)
                rList += _preOrderBST_Helper(root.left)
                rList += _preOrderBST_Helper(root.right)
            return rList
        return _preOrderBST_Helper(self.root)
    
    def postOrderBST(self):
        def _postOrderBST_Helper(root):
            rList = []
            if root:
                rList += _postOrderBST_Helper(root.left)
                rList += _postOrderBST_Helper(root.right)
                rList.append(root.val)
            return rList
        return _postOrderBST_Helper(self.root)

if __name__ == '__main__':
    print("Binary Search Tree Script")

    '''
    bst = BinarySearchTree()
    values = [-10,-3,0,5,9]
    for v in values:
        bst.insert(v)
    bst.printTree()
    

    inOrderList = bst.inOrderBST()
    print([inOrder for inOrder in inOrderList])

    preOrderList = bst.preOrderBST()
    print([preOrder for preOrder in preOrderList])

    postOrderList = bst.postOrderBST()
    print([postOrder for postOrder in postOrderList])
    '''
    bst1 = BinarySearchTree()
    root = None
    values = [-3,0,5,9,-6,14,13,-2]
    for v in values:
        root = bst1.insert(root, v)
    bst1.printTree()
    print("Root:",end=' ')
    print(bst1.getRoot().val)
    inOrderList = bst1.inOrderBST()
    print("Inorder:",end=' ')
    print([inOrder for inOrder in inOrderList])
    print("preOrder:",end=' ')
    preOrderList = bst1.preOrderBST()
    print([preOrder for preOrder in preOrderList])
    print("postOrder:",end=' ')
    postOrderList = bst1.postOrderBST()
    print([postOrder for postOrder in postOrderList])

