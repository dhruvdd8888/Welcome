# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    ans=0
    # lSum=0
    # rSum=0
    def maxPathSum(self, root) -> int:
        def postorder(root):
            if(root!=None):
                lsum=postorder(root.left)
                rsum=postorder(root.right)
                cmax=max(lsum,rsum,0)
                self.ans=(max(self.ans,cmax,cmax+root.val,lsum+rsum+root.val))
                # print(self.ans,cmax,lsum+rsum+root.val,cmax+root.val)
                # print(self.ans,root.val)
                return cmax+root.val
            return 0
        x=postorder(root)
        def negpost(root):
            if(root!=None):
                lsum=negpost(root.left)
                rsum=negpost(root.right)
                self.ans=max(self.ans,root.val)
        if(self.ans==0):
            self.ans=-1001
            negpost(root)
        return self.ans


x=Solution()
l=[5,4,8,11,None,13,4,7,2,None,None,None,1]
rrr=TreeNode(-60)
rl=TreeNode(-60)
rr=TreeNode(2,rrr,rl)
# llr=TreeNode(2)
# lll=TreeNode(7)
# ll=TreeNode(11,lll,llr)
pr=TreeNode(2,rr)#,None,p0)
pl=TreeNode(-6)
p=TreeNode(-3,pl,pr)

print(x.maxPathSum(p))


                # print(root.val,"=====")
                # rootSum=self.ans
                # postorder(root.left)
                # # l.append[root.val]
                # self.lSum+=root.val
                # if(self.lSum<0):self.lSum=0
                # # self.ans=(max(self.lSum,self.ans))
                # # print(self.lSum,self.ans,root.val)
                # # self.currSum-=root.val
                # postorder(root.right)
                # self.rSum+=root.val
                # if(self.rSum<0):self.rSum=0
                # self.ans=(max(self.rSum,abs(rootSum-self.lSum),self.ans))
                # print(self.rSum,abs(rootSum-self.lSum),rootSum,self.ans,root.val)
                # print("=====",root.val)