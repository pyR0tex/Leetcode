# return the maximum depth of a binary tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    print('iterative:')
    # appraoch 1: iterative solution
    # make a queue with root in it
    # while the queue exists append left and right leaves to the queue
    # raise the depth by 1 after all leaves have been appended on that level
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            for i in range(len(queue)):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return depth

    # approach 2: recursive (very intuitve!!!!)
    # if not node, return 0 for that recursive iteration
    # else => recur on the left and right leaves of that node and return + 1 of the maxs
    def maxDepth1(self, root: TreeNode) -> int:
        print('recursive:')
        if not root:
            return 0
        else:
            leftHeight = self.maxDepth(root.left)
            rightHeight = self.maxDepth(root.right)
        return 1 + max(leftHeight, rightHeight)

def main():
    S = Solution()
    root = TreeNode(3); root.left = TreeNode(9); root.right = TreeNode(20)
    l = root.left;
    r = root.right; r.left = TreeNode(15); r.right = TreeNode(7)
    result = S.maxDepth(root); print(result)
    result = S.maxDepth1(root); print(result)

if __name__ == '__main__':
    main()
