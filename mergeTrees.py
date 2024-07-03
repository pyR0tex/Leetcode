# merge 2 binary trees and return a single tree with merged nodes
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

    def printTree(self):
        if self.left:
            self.left.printTree()

        print(self.val, end = ' ')

        if self.right:
            self.right.printTree()

    def printPre(self):
        if self.val:
            print(self.val, end = ' ')
        if(self.left):
            self.left.printPre()
        if self.right:
            self.right.printPre()

root1, root2 = TreeNode(1),TreeNode(2)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)
root2.left = TreeNode(1)
root2.left.right = TreeNode(4)
root2.right = TreeNode(3)
root2.right.right = TreeNode(7)



# disregard all the extra definitions beside the init for TreeNode
# solution super easy
# basically just sum each node into the new tree and recur on left and right leaves

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        elif not root2:
            return root1
        else:
            rTree = TreeNode(root1.val + root2.val)
            rTree.left = self.mergeTrees(root1.left,root2.left)
            rTree.right = self.mergeTrees(root1.right,root2.right)
        return rTree

def main():
    S = Solution()
    rTree = TreeNode()
    rTree = S.mergeTrees(root1,root2)
    rTree.printPre()

if __name__ == "__main__":
    main()
