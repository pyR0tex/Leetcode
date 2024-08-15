# Binary Tree Class Implementation

from collections import deque

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val
    
    def __str__(self):
        return(f"{self.val}")
    
    def __repr__(self):
        return(f"val={self.val}, left={self.left}, right={self.right}")

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def getRoot(self) -> Node:
        if self.root:
            return self.root
        return None

    def CreateTree_LeetCode(self, nodes=None) -> Node:
        if not nodes: return None

        n = len(nodes)
        if n == 0: return  None

        self.root = Node(nodes[0])
        queue = deque([self.root])

        i = 1
        while i < n:
            cur = queue.popleft()
            if nodes[i] is not None:
                cur.left = Node(nodes[i])
                queue.append(cur.left)
            i += 1
            if i < n and nodes[i] is not None:
                cur.right = Node(nodes[i])
                queue.append(cur.right)
            i += 1
        return self.root


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
        '''
        HELPER FUNCTION TO VISUALIZE THE TREE
        '''

        if not self.root:
            print("Tree is empty")
            return

        def get_max_level(node):
            if not node:
                return 0
            return max(get_max_level(node.left), get_max_level(node.right)) + 1

        def print_level(level_nodes, level, max_level):
            if not any(level_nodes):
                return
            floor = max_level - level
            endge_lines = 2 ** max(floor - 1, 0)
            first_spaces = 2 ** floor - 1
            between_spaces = 2 ** (floor + 1) - 1

            print(' ' * first_spaces, end='')

            new_level_nodes = []
            for node in level_nodes:
                if node:
                    print(node.val, end='')
                    new_level_nodes.append(node.left)
                    new_level_nodes.append(node.right)
                else:
                    print(' ', end='')
                    new_level_nodes.append(None)
                    new_level_nodes.append(None)

                print(' ' * between_spaces, end='')

            print()
            for i in range(1, endge_lines + 1):
                for j in range(len(level_nodes)):
                    print(' ' * (first_spaces - i), end='')
                    if level_nodes[j] == None:
                        print(' ' * (endge_lines + endge_lines + i + 1), end='')
                        continue
                    if level_nodes[j].left:
                        print('/', end='')
                    else:
                        print(' ', end='')

                    print(' ' * (i + i - 1), end='')

                    if level_nodes[j].right:
                        print('\\', end='')
                    else:
                        print(' ', end='')

                    print(' ' * (endge_lines + endge_lines - i), end='')
                print()

            print_level(new_level_nodes, level + 1, max_level)

        max_level = get_max_level(self.root)
        print_level([self.root], 1, max_level)
        
    def inOrderBST(self, printList=False):
        def _inOrderBST_Helper(node):
            rList = []
            if node:
                rList += _inOrderBST_Helper(node.left)
                rList.append(node.val)
                rList += _inOrderBST_Helper(node.right)
            return rList
        inOrder = _inOrderBST_Helper(self.root)
        if printList:
            print(f"In-Order: {[_ for _ in inOrder]}")
        return inOrder
    
    def preOrderBST(self, printList=False):
        def _preOrderBST_Helper(root):
            rList = []
            if root:
                rList.append(root.val)
                rList += _preOrderBST_Helper(root.left)
                rList += _preOrderBST_Helper(root.right)
            return rList

        preOrder = _preOrderBST_Helper(self.root)
        if printList:
            print(f"Pre-Order: {[_ for _ in preOrder]}")
        return preOrder
    
    def postOrderBST(self, printList=False):
        def _postOrderBST_Helper(root):
            rList = []
            if root:
                rList += _postOrderBST_Helper(root.left)
                rList += _postOrderBST_Helper(root.right)
                rList.append(root.val)
            return rList

        postOrder = _postOrderBST_Helper(self.root)

        if printList:
            print(f"Post-Order: {[_ for _ in postOrder]}")
        return postOrder

if __name__ == '__main__':
    print("Binary Search Tree Script")
    
    tree = BinaryTree()
    root = None
    nodes = [3,9,20,None,None,15,7]

    root = tree.CreateTree_LeetCode(nodes)
    tree.printTree()

    inOrder = tree.inOrderBST()
    print(f"In-Order: {[_ for _ in inOrder]}")

    preOrder = tree.preOrderBST()
    print(f"Pre-Order: {[_ for _ in preOrder]}")

    postOrder = tree.postOrderBST()
    print(f"Post-Order: {[_ for _ in postOrder]}")