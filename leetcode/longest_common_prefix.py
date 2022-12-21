def longestCommonPrefix(strs) -> str:
    strs.sort(key=len)
    n=len(strs[0])
    first=strs[0]
    pr=0
    for j in range(1,n+2):
        flag=1
        for i in strs:
            print(j,"========",i[:j])
            if(i[:j]!=first[:j]):flag=0
        if flag:pr+=1
    print(pr)
    print(strs[0][:pr])

longestCommonPrefix(["dhrruv","dhrru","dhrru"])