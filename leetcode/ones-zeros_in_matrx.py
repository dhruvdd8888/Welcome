def onesMinusZeros(grid):
    l=len(grid)
    m=len(grid[0])
    # r,c=[],[]
    r=[2*sum(row) for row in grid]
    c = [2*sum(col)-l-m for col in zip(*grid)]
    # r.extend([0])
    # c.extend([0])
    # for i in range (l):
    #     for j in range(m):
    # c=[1,2,3]
    # r=[1,2,3]
    # print(r)
    # print(c)
    # ccc=2
    # ans=[ccc*x for x in [ccc*y for y in r]]
    # ans=[[((1000*r[x-1])+(100*y)+(10*m)+l) for y in c]for x in r]
    # ans=[]
    # for i in range (l):
        # ans.append[((1000*r[i])+(100*y)+(10*m)+l) for y in c]
        # ans.append([x + r[i] for x in c])
    ans=[[x + i for x in c]for i in r]
    return ans

print(onesMinusZeros([[0,1,1],[1,0,1],[0,0,1]]))
print(onesMinusZeros([[1,1,1],[1,1,1]]))
exit()
diff[i][j] = r[i] + c[j] - m+r[i] - l+c[j]