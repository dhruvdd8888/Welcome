class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recoverFromPreorder(traversal):
    root=TreeNode(traversal[0])
    traversal=traversal.replace("-","=-=")
    print(traversal)
    traversal=traversal.replace("-==-","--")
    traversal=traversal.replace("-==-","--")
    print(traversal)
    tl=traversal.split("=")
    # tl.append(None)
    print(tl)
    path=[root]
    for i in tl:
        if not i.isnumeric():
            dep=len(i)
            if(dep<len(path)):
                path=path[:dep]
        if not path[-1].left:
            path[-1].left=TreeNode(i)
            path.append(path[-1].left)
        else:
            path[-1].right=TreeNode(i)
            path.append(path[-1].right)
        
    return root
    # # while(traversal)
    # for i in range((len(list2)-1),-1,-1):
    #     he1= TreeNode(list2[i],x)
    #     x=he1


print(recoverFromPreorder("1-2--3--4-5--6--7"))