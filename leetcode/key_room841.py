def canVisitAllRooms(rooms) -> bool:
    n=len(rooms)
    q=set(range(1,n))
    nxt=set(rooms[0])
    for i in range(n):
        print(nxt,q)
        q=q.difference(nxt)
        nxt=set.union(set(),*map(set,[rooms[i] for i in nxt]))
    if(len(q)==0):return True
    return False
        # print(q)
        # nxt=set(rooms[nxt])
        # print(nxt)
        # print(rooms[nxt])
        # q=q.union(set(rooms[nxt]))
        # print(q)
    # return True

print(canVisitAllRooms( [[1],[2],[3],[]]))
print(canVisitAllRooms(  [[1,3],[3,0,1],[2],[0]]))