

def romanToInt(s: str) -> int:
    r2c={"I":1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    num=[]
    length=len(s)
    for i in range(length):
        num.append(r2c[s[i]])
    number=0
    for i in range (length-1):
        if(num[i]>=num[i+1]):
            number+=num[i]
        else:
            number-=num[i]
    number+=num[-1]
    return number
print("=========",romanToInt("MMMCMXCIXII"))