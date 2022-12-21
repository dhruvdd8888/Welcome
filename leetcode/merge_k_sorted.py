
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    ls=[]
    for k in lists:
        i=k
        while i:
            ls.append(i.val)
            i=i.next
        lists.extend(ls)
        lists.remove(k)
    lists.sort()
    lists=[1,2]
    he2=None
    x=None
    for i in range((len(lists)-1),-1,-1):
        he2= ListNode(lists[i],x)
        x=he2

    print(he2.next.val)
    print(he2)



