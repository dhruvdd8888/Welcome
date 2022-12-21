def checkValid(matrix) -> bool:
    n=len(matrix)
    s=set(range(1,n+1))
    for i in range(n):
        if(set(matrix[i])!=s):return False
    matrix=list(zip(*matrix))
    for i in range(n):
        if(set(matrix[i])!=s):return False
    return True