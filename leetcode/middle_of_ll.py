class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    hd=head
    ans=head
    n=0
    while(hd):
        n+=1
        if(n%2==0):ans=ans.next
        # print(hd.val,end="--")
        hd=hd.next
    # print(n)
    # n=int(n/2)
    # hd=head
    # while(n):
    #     hd=hd.next
    #     n=n-1
    return ans.val 



list2=[1]
he1=None
x=None
for i in range((len(list2)-1),-1,-1):
    he1= ListNode(list2[i],x)
    x=he1
print(middleNode(he1))