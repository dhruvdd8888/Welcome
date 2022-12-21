class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head) :
        if(head==None):return head
        h=head
        pre=None
        nxt=None
        while(h!=None):
            nxt=h.next
            h.next=pre
            pre=h
            h=nxt
        printer(pre)
        return pre

def printer(head):
    print("")
    while(head!=None):
        print(head.val,end="->")
        head=head.next



list2=[1,2,3,4,5,6]
# list2=[1,3]
list2=[3]
# list2=[]

he1=None
x=None
for i in range((len(list2)-1),-1,-1):
    he1= ListNode(list2[i],x)
    x=he1
print(reverseList(he1))
