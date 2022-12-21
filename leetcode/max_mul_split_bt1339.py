# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def maxProduct( root):
    
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        def nodetot(root):
            if root is None:
                return 0
            return root.val + nodetot(root.left) + nodetot(root.right)
        
        def dfs(node):
            if node!=None:
                if node.left is None and node.right is None:
                    self.high = max(self.high, (node.val * (self.total - node.val)))
                    return node.val
                curr = node.val + dfs(node.left) + dfs(node.right)
                self.high = max(self.high, (curr * (self.total - curr)))
                return curr
        
        total = nodetot(root)
        high = 0
        dfs(root.left)
        dfs(root.right)
        return self.high % (10**9 + 7)

