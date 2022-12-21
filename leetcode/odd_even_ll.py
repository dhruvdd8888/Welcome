class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head ):
    if(head==None):return None
    hd=head
    n=1
    while(hd.next):
        hd=hd.next
        n+=1
    fh=head
    t=head.next
    for i in range (int(n/2)):
    # while():
        hd.next=fh.next
        hd=hd.next
        fh.next=fh.next.next
        print("f")
        fh=fh.next
    # print(hd.val,"====",hd.next.val,"====",fh.val,"======",fh.next.val)
    # fh.next=t
    hd.next=None
    hd=head
    while(hd):
    # for i in range (n):
    # while(hd.next):
        print(hd.val,end="..")        
        hd=hd.next
    return head
# 135246
# list2=[1,2,3,4,5,6,7,8,9,10]
list2=[]
he1=None
x=None
for i in range((len(list2)-1),-1,-1):
    he1= ListNode(list2[i],x)
    x=he1
print(oddEvenList(he1))
# 3222222222