def isValid(s: str) -> bool:
    l=[]
    for i in s:
        if(i=="[" or i=="{" or i=="("):l.append(i)
        elif(len(l)==0):return False
        elif(i=="]" and l[-1]=="["):l=l[:-1]
        elif(i=="}" and l[-1]=="{"):l=l[:-1]
        elif(i==")" and l[-1]=="("):l=l[:-1]
        else: return False
    if(len(l)==0):return True
    return False
print(isValid("())"))