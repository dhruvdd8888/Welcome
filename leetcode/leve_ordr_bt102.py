sr="TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}"
sr="TreeNode{val: 0, left: TreeNode{val: 2, left: TreeNode{val: 1, left: TreeNode{val: 5, left: None, right: None}, right: TreeNode{val: 1, left: None, right: None}}, right: None}, right: TreeNode{val: 4, left: TreeNode{val: 3, left: None, right: TreeNode{val: 6, left: None, right: None}}, right: TreeNode{val: -1, left: None, right: TreeNode{val: 8, left: None, right: None}}}}"
sr=sr.replace("TreeNode","")
sr=sr.replace("val:","")
sr=sr.replace("left:","")
sr=sr.replace("right:","")
sr=sr.replace("None","")
sr=sr.replace(" ","")
sr=sr.replace(",","")

dp=-1
ss=""
l=[]
for i in sr:
    if(i=="{"):
        l.append([])
        # print(ss)
        if(ss.isnumeric() or (ss and ss[0]=="-")):l[dp].append(int(ss))
        ss=""
        dp+=1
    elif(i=="}"):
        # print(ss)
        if(ss.isnumeric() or (ss and ss[0]=="-")):l[dp].append(int(ss))
        ss=""
        dp-=1
    else:
        # l[dp].append(i)
        ss+=i
l=[i for i in l if(len(i))]
print(sr)
print(l)
print([[0],[2,4],[1,3,-1],[5,1,6,8]])