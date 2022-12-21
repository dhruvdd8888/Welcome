# for i in range(0,-1,-1):
    # print(i)

# from math import log10

# print((2**31-1))

# st="Ten thousand Ten One Sit Ten Five"

# st=st.replace("Ten One","Eleven")
# st=st.replace("Ten Five","Fifteen")

# print(st)

# a=12
# b=2
# x=(b|a) 
# x=bin(x).replace("0b", "0")
# print(x)
# l=list(map(int, x.strip()))
# print(l)
# x= sum(list(map(int, x.strip())))
# # x=sum(list_of_number)
# print(x)
# 1100
# 0010


# ans=[1,2,4,4,4,4,10,7,1,2,3,3]
# ans = [*set(ans)]
# print(ans)

# ans=5
# ans+=1
# ans-=0.5
# print(ans)


# ans=0
# number=12|4
# while ( number ):
#     ans += (number&1)
#     number = number >> 1
# print(ans)



# i=2
# j=20003
# z=i
# w=j
# x = sum(list(map(int,(bin(i|j).replace("b","")).strip())))
# y = sum(list(map(int,(bin(i&j).replace("b","")).strip())))
# t= sum(list(map(int,(bin(z).replace("b","")).strip())))
# t+=sum(list(map(int,(bin(w).replace("b","")).strip())))
# if((x+y)==t):
#     print(x+y)



# def entry(nums,x):
#     n=len(nums)
#     # flag=0
#     s=0
#     e=n-1
#     while(s<=e):
#         m=int((s+e)/2)
#         if(nums[m]==x ):
#             if(m==0 or nums[m-1]!=x):
#                 return m
#         if(nums[m]>=x):
#             e=m-1
#             # if(s==n):flag=1
#         if(nums[m]<x):
#             s=m+1
#     if(nums[m]>x):
#         print(n-m)
#         print(nums[m-1],"--------")
#         return m-1
#     return m    

    # print(nums.index(x))

# nums=[1,3,3,3,3,6,7,7,7,7,10,13]
# # nums=[*set(nums)]
# print(nums)
# print(entry(nums,16))





# x=5
# if(x==5):
#     x=x*"aa"
#     print(x,"c")
# elif(x>0):
#     print("c")



# l=[23,31]
# l.append(6)
# print(l)

# days=[1,2,3,4]
# done=[1,2,4,5,6,7]
# for i in range (0,len(days)):
#         if days[i] in done: continue
#         else:print("ec")    
#         print("ccc",days[i])






# l=[1,23,4]
# # a=(*l)
# print(sum(list(filter(lambda x: (x),l))))
# print(a)



# l=[1,3,5]
# old=l[0]
# old+=10
# print(l)


# n=j=4
# print(n,j)

# l=[1,2,4,6]
# x=sum(l)
# print(x)



# dic={"a":0,"b":2,"c":1}
# print(max(dic, key= lambda x: dic[x]))

# print(-2%3)


# l=[[1,2,3],[4,5,6],[7,8,9]]

# x=[j for j in [1,2,4]]
# mat = [[[1,3,2] for x in y] for y in l]

# r=[1000,22,4]
# c=[70,8880,90]
# mat=[]
# for i in range(3):
#     mat.append([x + r[i]+1000 for x in c])
# maat=[[x + i+1000 for x in c]for i in r]
# print(mat)
# print(maat)
# print(maat==mat)




# s = 'Geeks123For123Geeks'
# x="123"
# print(s.translate({ord(i): None for i in x}))




# z=")"
# y="]"
# z="}"
# d={"(":z,"[":y,"{":x}




# s="dhruvdhana"
# t="d"
# for i in range(len(s)):
#     if(s[i]==t):
#         fs=s[:i]+s[i+1:]
#         print(fs)



# l=['()()', '()(())', '()()()', '(())']
# l.sort(key=len,reverse=True)
# ml=len(l[0])
# for i in range(len(l)):
#     if(len(l[i])<ml):wrg=i-1
# print(l[:wrg])



# ans=123
# res = list(map(int, str(ans)))
# # s=str(ans)
# # li=[s.split()]
# res.reverse()
# print(res)


# nums=[1,2,3,4,5,6,98]
# nums[:3]=0,0,0
# print(nums)



# for i in range(5):print(i,end=" ")
# for i in range(i,10):print(i,end=" ")



# n=5
# print(int(n/2+1))



# x=5
# y=x
# y=3
# print(x,y)

# s='''
# x=5
# y=x
# y=3
# print(x,y)
# return 1
# '''
# # print(exec(s))


# global start

# def rangeSumBST() -> int:

#     def traverse():
#         print(start,end="==")
#         start-=1
#     traverse()
#     return start

# print(rangeSumBST())






# def removeInvalidParentheses(s: str) :
#     def isValid(s: str) -> bool:
#         l=[]
#     def check(s):
#         if(True):answer.append(8)           #list could be called but not int
#     answer=[9]
#     check("dhruv")
#     return answer

# print(removeInvalidParentheses("dhr"))




# m=max(int)
# print(m)


# li=[1,2,1,1,44,1,45,1]
# # print(li)
# print(li.count(1))
# li=[i for i in li if i!=1]
# # li.remove(1)
# li.extend([1]*8)
# print(li)

# l=[1,2,4,5,6,7,8]
# l2=[1,1,1,1,1,1,1]
# l=[(i-j) for i,j in zip(l,l2)]
# print(l)


# l=[-9,-2,1,2,4,5,6,7,8]
# i=[i for i in range (len(l)) if l[i]>0]
# print(i[0])


# print(301/2,type(301/2))
# print(301//2,type(301//2))

# print(7+11+8+5+4+13+1)

# print(max(-10,-199))



# print(9<10<12)

# a=2
# b=1
# c=4

# if(a<b):
#     if(a<c):
#         print(a)
#     else:
#         print(c)
# else:
#     if(b<c):
#         minpath(i+1,j+1)
#     else:
#         minpath(i+1,j-1)



# nums=[1,3,4,5]
# __add(3)__nums
# nums=[i-1 for i in nums]
# print(nums)



# print(3+3//2)


# s={1,2,3,4,5,6,7,8,9}
# y=[1,2,None,None,None,2]

# print(s-set(y))


# x=[1,2,3]
# print(x[1::-1])





# l=list([[None]*5]*4)
# for i in range(5):
#     for j in range(4):
#         l[j][i]=i*10+j  
# print(l)


# x=3
# while(x<4):
#     try:
#         print(x)
#         # x=x-1000000000000000000000
#     except:
#         print("bs")
#         exit()
#     # print("no")








# s={2,4,6,7}
# s=s.difference({1,2,3,4})
# print(s)


# l= [[1,3],[3,0,1],[2],[0]]
# nxt={1,3}
# nnn=set.union(*map(set,[l[i] for i in nxt]))
# print(nnn)
# nxt=set.union({l[i] for i in {1,2}})



# ss=""
# if(ss.isnumeric() or ss and ss[0]=="-"):
#     print(ss)
#     print(int(ss))


g2=[1,2,3,4]
g3=[1,2]
for i in g3:g2.remove(i)
print(g2)

