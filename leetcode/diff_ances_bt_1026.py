# start=[]N
# diff=[]
# # Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    ans=0

    def maxAncestorDiff(self, root):
        self.ans=0
        def traverse( root, lnode, hnode):
            if root:
                self.ans = max(self.ans, abs(root.val - lnode) , abs(root.val-hnode) )
                if root.val < lnode:
                    lnode = root.val
                if root.val > hnode:
                    hnode = root.val
                traverse(root.left, lnode, hnode)
                traverse(root.right, lnode, hnode)
        traverse(root, root.val, root.val)
        return self.ans





#     start=[]
#     diff=[]
#     def maxAncestorDiff(self, root) -> int:
#         def traverse(curr):
#             if(curr):
#                 self.start.append(curr.val)
#                 if(curr.left):
#                     print(curr.val,end="=======")
#                     print(self.start)
                    
#                     self.diff.extend([abs(curr.val-i) for i in self.start])
#                     traverse(curr.left)
#                     # start=[]
#                     self.start=self.start[:-1]
#                 if(curr.right):
#                     traverse(curr.right)

#                     # self.start.append(curr.val)
#                     print(curr.val,end="=======")
#                     print(self.start)
#                     self.diff.extend([abs(curr.val-i) for i in self.start])
#                     self.start=self.start[:-1]

#         traverse(root)
#         print()
#         # print(self.start)
#         print(self.diff)
#         self.start=[]
#         ab= max(self.diff)
#         self.diff=[]
#         return ab

# def recoverFromPreorder(traversal):
#         traversal=traversal.replace("-","=-=")

#         traversal=traversal.replace("-==-","--")
#         traversal=traversal.replace("-==-","--")

#         tl=traversal.split("=")

#         root=TreeNode(tl[0])
#         path=[root]
#         tl=tl[1:]


#         for i in tl:
#             if not i.isnumeric():
#                 dep=len(i)
#                 if(dep<len(path)):
#                     path=path[:dep]
#                 continue
#             if not path[-1].left:
#                 path[-1].left=TreeNode(i)
#                 path.append(path[-1].left)
#             else:
#                 path[-1].right=TreeNode(i)
#                 path.append(path[-1].right)
            
#         return root
#     # # while(traversal)
#     # for i in range((len(list2)-1),-1,-1):
#     #     he1= TreeNode(list2[i],x)
#     #     x=he1



x=Solution()

# print(x.maxAncestorDiff(p))
# p3=TreeNode(3)
# p0=TreeNode(0,p3)

p2=TreeNode(222)#,None,p0)
p=TreeNode(111,None,p2)
# p.right=p2
print(x.maxAncestorDiff(p))
print(x.maxAncestorDiff(p))





exit()


















self.ans=0
def maxAncestorDiff(self, root):
    self.traverse(root, root.val, root.val)
    return self.ans

def traverse(self, root, lnode, hnode):
    if not root:
        return
    self.ans = max(self.ans, abs(root.val - lnode) , abs(root.val-hnode) )
    if root.val < lnode:
        lnode = root.val
    if root.val > hnode:
        hnode = root.val
    self.traverse(root.left, lnode, hnode)
    self.traverse(root.right, lnode, hnode)