def numberToWords(num: int) -> str:
    answer=""
    a=[["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"],
    ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"],
    ["Thousand","Million","Billion"]]
    flag=1
    x=0
    while(num):
        t=num%10
        num=int(num/10)
        if(flag==1):
            if t :answer=a[0][t]+" "+answer
            flag=2
            continue
        if(flag==2):
            if t :answer=a[1][t]+" "+answer
            flag=3
            continue
        if(flag==3):
            if t :answer=a[0][t]+" Hundred "+answer
            flag=4
            continue
        if(flag==4):
            if t:answer=a[0][t]+" "+a[2][x]+" "+answer
            if not t and num%100 :answer=a[2][x]+" "+answer
            x+=1
            flag=2

    answer=answer.replace("Ten One","Eleven")
    answer=answer.replace("Ten Two","Twelve")
    answer=answer.replace("Ten Three","Thirteen")
    answer=answer.replace("Ten Four","Fourteen")
    answer=answer.replace("Ten Five","Fifteen")
    answer=answer.replace("Ten Six","Sixteen")
    answer=answer.replace("Ten Seven","Seventeen")
    answer=answer.replace("Ten Eight","Eighteen")
    answer=answer.replace("Ten Nine","Nineteen")
    if not len(answer):return "Zero"
    return answer[:-1]


print("-------",(numberToWords(102222200)),"-----")
