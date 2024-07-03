# 110. Balanced Binary Tree
from BinarySearchTree import Node



def isBalanced(root: Node) -> bool:
    print("Balanced Binary Tree?")
    '''
    
    THIS IS A DFS Solution
    
    '''
    def depth(node):
        if not node:
            return 0
        
        leftDepth = depth(node.left)
        if leftDepth == -1:
            return -1
        
        rightDepth = depth(node.right)
        if rightDepth == -1:
            return -1
        
        if abs(leftDepth - rightDepth) > 1:
            return -1
        return max(leftDepth, rightDepth) + 1
    

    return depth(root) != -1

if __name__ == '__main__':
    root = Node(6)
    isBal = isBalanced(root)
    print("Is Balnaced: " + str(isBal))