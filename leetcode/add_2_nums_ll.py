# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1, l2) :
        n1=0
        t1=1
        t2=1
        n2=0
        while(l1):
            n1+=l1.val*t1
            t1*=10
            print(l1.val)
            l1=l1.next
        while(l2):
            n2+=(l2.val*t2)
            t2*=10
            print(l2.val)
            l2=l2.next
        ans=n1+n2
        
        ans=123
        res = list(map(int, str(ans)))
        res.reverse()
        he2=None
        x=None
        for i in range((len(lists)-1),-1,-1):
            he2= ListNode(res[i],x)
            ans=int(ans/10)
            x=he2
        return(he2)


lists=[5,6,4]
he2=None
x=None
for i in range((len(lists)-1),-1,-1):
    he2= ListNode(lists[i],x)
    x=he2
    
list2=[2,4,3]
he1=None
x=None
for i in range((len(list2)-1),-1,-1):
    he1= ListNode(list2[i],x)
    x=he1

print(addTwoNumbers(he2,he1))