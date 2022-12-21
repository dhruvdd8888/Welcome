class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def delMiddleNode(head):
    if(head.next==None):return None
    hd=head
    ans=head
    n=0

    while(hd.next):
        n+=1
        hd=hd.next
        if(n%2==0 and hd.next!=None):ans=ans.next
    ans.next=ans.next.next
    return head 



list2=[7]
he1=None
x=None
for i in range((len(list2)-1),-1,-1):
    he1= ListNode(list2[i],x)
    x=he1
print(delMiddleNode(he1))