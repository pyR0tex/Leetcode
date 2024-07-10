# 112. Path Sum
'''
Given the root of a binary tree and an integer targetSum,
return true if the tree has a root-to-leaf path such that adding up 
all the values along the path equals targetSum.
'''


from BinarySearchTree import BinaryTree

def HasPathSum(root, targetSum: int) -> bool:
    print("     -- Path Sum --")
    def _helper(node, target):
        if not node:
            return False
        target -= node.val
        if not node.left and not node.right:
            return target == 0
        return _helper(node.left, target) or _helper(node.right, target)
    
        
    return _helper(root, targetSum)


if __name__ == '__main__':
    tree = BinaryTree()
    nodes = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    root = tree.CreateTree_LeetCode(nodes)
    tree.printTree()

    target = 22
    hasPathSum = HasPathSum(root, target)
    print(f"Has Path Sum?      {hasPathSum}, should return True")