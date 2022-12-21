def frequencySort(s: str) -> str:
    # dic={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    # dic=list(s)
    # for i in s:dic.append(i)
    # y=[dic, key= lambda x: dic[x]]
    # y=[]
    # y.append(dic, key= lambda x: abs(dic[x]))
    # print(y)
    # print(max(dic, key= lambda x: abs(dic[x])))
    # res=""
    # res=res.join(sorted(dic, key = dic.count,reverse = True))
    li=list(s)
    # li.sort()
    from collections import Counter
    x=""
    # xx=li.sort(key=li.count)
    # print(li)
    # xx=[key for key, value in Counter(li).most_common()]
    return x.join([i for j, c in Counter(li).most_common()for i in [j] * c])
    # print(x.join(xx))

    # return (x.join(sorted(li, key = li.count,reverse = True)))
 

print(frequencySort("loveleetcode"))