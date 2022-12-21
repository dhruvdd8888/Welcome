def myAtoi(s):
        l=[str(i) for i in range(10)]
        l2=["-","+"]
        ans=""
        try:
            while(s[0]==" "):s=s[1:]
        except:return 0
        for i in range(len(s)):
            if(s[i] in l2):
                ans+=s[i]
                l2=[]
                continue
            if(s[i] in l):
                ans+=s[i]
            else:break
        try:
            if(int(ans)>2147483647):return 2147483647
            if(int(ans)<-2147483648):return -2147483648
            return int(ans)
        except:
            return 0
s="c0024words and 987"
s="  +28 42"
s="-5-44"
print(myAtoi(s))


# print(int("  "))
# class cars:
#     now=0
#     def wheels(self,s):
#         print(now)


# x=cars()
# x2=cars()
# x3=cars()

# x.wheels("sfvbgn")