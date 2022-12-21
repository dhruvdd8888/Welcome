def evalRPN(tokens: list[str]) -> int:
    ans=[]
    for i in range(len(tokens)):
        t=tokens[i]
        if(t.isnumeric() or t[0]=="-"):ans.append(int(t))
        else:
            n2=ans.pop(-1)
            n1=ans.pop(-1)
            if(t=="*"):
                a=n1*n2
                ans.append(a)
            elif(t=="+"):
                a=n1+n2
                ans.append(a)            
            elif(t=="/"):
                a=int(n1/n2)
                ans.append(a)            
            else:
                a=n1-n2
                ans.append(a) 

    return ans[0]

s=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
s=["10","6","+","9","*"]
s=["4","13","5","/","+"]
s=["2","1","+","3","*"]
print(evalRPN(s))
