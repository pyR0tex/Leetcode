# given the root of a binary tree, return true if it is a mirror of itself else false

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if self.val:
            if val <= self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
            elif val >= self.val:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val


    def inOrder(self):
        if self.left:
            self.left.inOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.inOrder()

    def preOrder(self):
        if self.val:
            print(self.val)
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

############
# both approaches perform around the same. Very intuitive
# Almost had the recursive down by yourself
# need more work, think smart
############
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # approach 1: recursive dfs solution
        # check if root exists and call sym with left and right nodes
        # check if left and right exist => check vals and call sym with correct logic
        print('recursive:')
        if not root:
            return True
        def sym(left,right)->bool:
            if left and right:
                return left.val == right.val and sym(left.left,right.right) and sym(left.right,right.left)
            return left == right

        return sym(root.left,root.right)

    # approach 2: iterative solution
    # use stack to hold left and right nodes as a tuple and pop them
    # if not left and not right => continue to pop stack because they are None
    # if line 68 condition met, return False.
    def isSymmetric1(self, root: TreeNode) -> bool:
        print('iterative:')
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            stack.append((left.left,right.right))
            stack.append((left.right,right.left))
        return True

        
def main():
    S = Solution()
    root = TreeNode(1); root.left = TreeNode(2); root.right = TreeNode(2)
    l = root.left; l.left = TreeNode(3); l.right = TreeNode(4)
    r = root.right; r.left = TreeNode(4); r.right = TreeNode(3)
    root.inOrder(); print('')

    flag = S.isSymmetric(root);print(flag)
    flag = S.isSymmetric1(root);print(flag)

if __name__ == '__main__':
    main()
