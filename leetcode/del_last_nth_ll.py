class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head,n): 
    if(head.next==None):return None
    ans=head
    n+=2
    com="ans"+".next"*n
    try:
        while(exec(com)==None):
            ans=ans.next
    except:

        try:
            n-=1
            com="ans"+".next"*n
            exec(com)
        except:
            return head.next
        ans.next=ans.next.next
        return head

list2=[1,2,3,4,5,6,7,8,9]
he1=None
x=None
for i in range((len(list2)-1),-1,-1):
    he1= ListNode(list2[i],x)
    x=he1
print(removeNthFromEnd(he1,9))