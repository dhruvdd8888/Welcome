# answer=[]
def removeInvalidParentheses(s: str) :
    # clo=["}","]",")"]
    def isValid(s: str) -> bool:
        l=[]
        for i in s:
            if(i>="a" and i<="z"):continue
            elif(i=="[" or i=="{" or i=="("):l.append(i)
            elif(len(l)==0):return i
            elif(i=="]" and l[-1]=="["):l=l[:-1]
            elif(i=="}" and l[-1]=="{"):l=l[:-1]
            elif(i==")" and l[-1]=="("):l=l[:-1]
            else: return l[-1]
        if(len(l)==0):return True
        return l[-1]
    # def corrector(s,t):

    #     #([]()
    #     print(t)
    #     # print(s)
    #     if(t in clo):
    #         for i in range(len(s)):
    #             if(s[i]==t):
    #                 fs=s[:i]+s[i+1:]
    #                 # print(i)
    #                 if(isValid(fs)==True):answer.append(fs)
    #                 elif(len(answer)==0):
    #                     print(i)
    #                     removeInvalidParentheses(fs)
    #     else:
    #         for i in range(len(s)):
    #             if(s[i]==t):
    #                 fs=s[:i]+s[i+1:]
    #                 # print(i)
    #                 if(isValid(fs)==True):answer.append(fs)
    #                 elif(len(answer)==0):
    #                     print(i)
    #                     removeInvalidParentheses(fs)

    # t=isValid(s)
    # if(t==True):
    #     answer.append(s)
    #     # print(s)
    #     return

    # corrector(s,t)
    # l=answer
    # l.sort(key=len,reverse=True)
    # ml=len(l[0])
    # wrg=0
    # print(answer)
    # for i in range(len(l)):
    #     if(len(l[i])<ml):
    #         wrg=i
    #         break
    # # print(l[:wrg])
    # return (answer[:wrg])

    # zz="("
    # yy="["
    # xx="{"
    # d={")":zz,"]":yy,"}":xx}
    # s=(s.translate({ord(i): None for i in d[t]}))
    # print("-----,",s)
    def check(s):
        l=[]
        flag=0
        futFlag=0
        for i in range (len(s)):
            if(s[i]>="a" and s[i]<="z"):continue
            elif(s[i]=="[" or s[i]=="{" or s[i]=="("):l.append(s[i])
            elif(len(l)==0):#()))
                t=s[i]
                for j in range(len(s)):
                    if(s[j]==t):
                        fs=s[:j]+s[j+1:]
                        # print(i)
                        if(isValid(fs)==True):
                            answer.append(fs)
                            flag=1
                        else:
                            futFlag=check(fs)
                            if(futFlag==1):return 1
            elif(s[i]=="]" and l[-1]=="["):l=l[:-1]
            elif(s[i]=="}" and l[-1]=="{"):l=l[:-1]
            elif(s[i]==")" and l[-1]=="("):l=l[:-1]
        print(s)
        if(len(l)==0 and isValid(s)==True):answer.append(s)
        
        for i in range (len(s)):
            if(s[i]>="a" and s[i]<="z"):continue
            elif(s[i]=="[" or s[i]=="{" or s[i]=="("):l.append(s[i])
            elif(len(l)!=0):#(()
                # for k in ()
                # print("not=========",s,"========",l)
                t=l[-1]
                #     t=s[i]
                for j in range(len(s)-1,-1,-1):
                    if(s[j]==t):
                        fs=s[:j]+s[j+1:]
                        # print("\\\\\\\\",fs)
                        if(isValid(fs)==True):
                            answer.append(fs)
                            flag=2
                        else:
                            futFlag=check(fs)
                            if(futFlag==2):return 2
                        
        return flag

    answer=[]
    check(s)
    print(answer)
    if(len(answer)!=0):
        answer=list(set(answer))
        answer.sort(key=len,reverse=True)
        ml=len(answer[0])
        wrg=len(answer)
        for i in range(len(answer)):
            if(len(answer[i])<ml):
                wrg=i
                break
        return answer [:wrg]
    s=s.replace("(","")
    s=s.replace(")","")
    return [s]

    # return answer
    # return list(set(answer))

# print(removeInvalidParentheses("()(a()(sfg)"))
print(removeInvalidParentheses("())k)())"))

# print(answer)

# ())a()(sfg)