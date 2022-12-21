# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val: int) :

        #check if empty
        if(head==None):return None

        #removes val if in head
        while(head.val==val):
            if(head.next==None):
                return None
            head=head.next
        if(head==None):return None
        t=head
        tp=head

        #removes val if in middle
        while(t.next!=None):
            if(t.val==val):
                while(t.val==val):
                    v=t.next
                    t=t.next
                tp.next=v
            tp=t
            t=t.next

        #removes val at end
        if(tp.val==val):
                tp.next=None
            
        return head


        
def printer(head):
    print("")
    while(head!=None):
        print(head.val,end="->")
        head=head.next

list2=[9,9,9,1,2,3,9,9,9,9,4,5,6,9,9,9,9,6,9,9,9,0]
he1=None
x=None
for i in range((len(list2)-1),-1,-1):
    he1= ListNode(list2[i],x)
    x=he1
# print(isPalindrome(he1))
printer(removeElements(he1,9))