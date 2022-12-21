def strWithout3a3b(a: int, b: int) -> str:
    import math
    if(a*0.5==b):
        ans=b*"aab"
    elif(b*0.5==a):
        ans=a*"bba"
    elif(a==b):
        ans=a*"ab"
    elif(b<(a*0.5)):
        ans=math.ceil(a/2)*"aab"
        if(b+1==(a*0.5) and a&1 ):return(ans[:-2])
        if (not b+1==(a*0.5) and a&1):return ans[:-2]
        if(b+1==(a*0.5)):return ans[:-1]
    elif(a<(b*0.5)):
        ans=math.ceil(b/2)*"bba"
        if(a+1==(b*0.5) and b&1 ):return(ans[:-2])
        if (not a+1==(b*0.5) and b&1):return ans[:-2]
        if(a+1==(b*0.5)):return ans[:-1]
    elif(a>b):
        ans=int(b*0.5)*"aabb"
        for i in range(a-b):
            ans=ans.replace("aa","aba")
    elif(b>a):
        ans=int(a*0.5)*"aabb"
        for i in range(b-a):
            ans=ans.replace("bb","bab")
    return(ans)
print(strWithout3a3b(1,4))

# aabaabaa