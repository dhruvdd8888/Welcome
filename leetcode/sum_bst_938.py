# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(root, low, high) -> int:
    def traverse(curr):
        if(curr):
            traverse(curr.left)
            if(low<=curr.val and high>=curr.val):start.append(curr.val)
            traverse(curr.right)
    start=[]
    traverse(root)
    return sum(start)

