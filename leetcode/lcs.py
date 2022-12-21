def longestCommonSubsequence( text1: str, text2: str) -> int:
        n1=len(text1)+1
        n2=len(text2)+1
        l=[[0]*n2 for i in range(n1)]
        for i in range(n1):
            for j in range(n2):
                if(i==0 or j==0):
                    l[i][j]=0
                elif(text1[i-1]==text2[j-1]):
                    l[i][j]=(l[i-1][j-1]+1)
                else:
                    if(l[i-1][j]<l[i][j-1]):
                        l[i][j]=(l[i][j-1])

                    else:
                        l[i][j]=(l[i-1][j])
        return l[n1-1][n2-1]

def longetCommonSubsequence( text1: str, text2: str) -> int:
    n1=len(text1)+1
    n2=len(text2)+1
    # l=list([[0]*n2]*n1)
    l=[[[0,0] for j in range(n2)] for i in range(n1)]
    # l=[[[0, 4], [0, 4], [0, 4], [0, 4], [0, 4]],
    #  [[0, 4], [0, 4], [0, 4], [0, 4], [0, 4]],
    #   [[0, 4], [0, 4], [0, 4], [0, 4], [0, 4]],
    #    [[0, 4], [0, 4], [0, 4], [0, 4], [0, 4]]]
    # for i in range(n1):
            # l.append([0]*n2)
    print(l)
    # ll=[]
    # l[1][1][0]=99
    print(l)
    # return 0
    for i in range(n1):
        for j in range(n2):
            if(i==0 or j==0):
                print(i,j)
                l[i][j][0]=0
                # continue
                # print(l[i])
            elif(text1[i-1]==text2[j-1]):
                # print(text1[i-1],end=" ")
                # print(l[i][j])
                # print(i,j)
                l[i][j][0]=(l[i-1][j-1][0]+1)
                l[i][j][1]="*"
            else:
                if(l[i-1][j][0]<l[i][j-1][0]):
                    l[i][j][0]=(l[i][j-1][0])
                    l[i][j][1]="-"

                else:
                    l[i][j][0]=(l[i-1][j][0])
                    l[i][j][1]="|"
        # ll.append(l[i])
        # print(l[i])
        # ll=l[i+1]
    for i in range(n1):print(l[i])
    i=n1-1
    j=n2-1
    print(i,"===========",j)
    ans=""
    while(i>1 or j>1):
        print(i,j)
        if(l[i][j][1]=="|"):i-=1
        elif(l[i][j][1]=="-"):j-=1
        else:
            print(i,j, text1[i-1])
            ans=text1[i-1]+ans
            i-=1
            j-=1
    return ans


    # print(l)
    # print("........")
    # print(l)
    # l[0][0]=-1
    # while(i!=0 or j!=0):
    #     if()

text2 = "labc"
text1 = "lab" 
# text2 = "prov"
# text1 = "pre" 
print(longestCommonSubsequence(text1,text2))
print(longetCommonSubsequence(text1,text2))