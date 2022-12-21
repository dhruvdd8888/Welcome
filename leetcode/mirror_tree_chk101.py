# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        def indr(d,root):      
            if not root:return
            indr(-1,root.left)
            tr.append([root.val,d])
            indr(1,root.right)
        tr=[]
        d=1
        indr(d,root)
        for i in range(len(tr)//2):
            tr[i][1]*=-1
        if(tr!=tr[::-1]):return False
        return True