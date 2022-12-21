import random
x=random.randint(1,100000000)
z=int(((x+1)%10)%2==0)+2

x=random.randint(1,100000000)
x=x%z==0
print(x)
# for i in range(7):
#     l=0
#     lll=0
#     # for i in range(0,500):
#     for i in range(10001):
#             z=random.randint(0,100000)
#             if(z%2==0):
#                 l+=1
#             else:l-=1
#         # if(l>0):
#         #     lll+=l&l-100
#         #     # if():
#             #     lll+=(l+1)%10


#     print(l%2==0)

# exit()
# y=random.randint[2:3]
# if(x%y==0):
#     print("do")
# else:
#     print("dont")