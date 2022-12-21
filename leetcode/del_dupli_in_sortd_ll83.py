
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    if(head==None):return None
    h=head

    while(h!=None and h.next!=None):
        n=h.next
        t=h
        try:
            while(h.val==t.val):
                t=t.next
        except:pass
        h.next=t
        h=t
    
    printer(head)
    return head

def printer(head):
    print("")
    while(head!=None):
        print(head.val,end="->")
        head=head.next



list2=[0,0,0,1,1,1,1,1,1,1,1,1,2,3,4,5,5,5,5,6,6,6,9]
# list2=[1,3]
# list2=[3]
# list2=[]

he1=None
x=None
for i in range((len(list2)-1),-1,-1):
    he1= ListNode(list2[i],x)
    x=he1
print(deleteDuplicates(he1))
