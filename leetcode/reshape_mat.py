def matrixReshape(mat, r: int, c: int):
        m=len(mat)
        n=len(mat[0])
        if(m*n!=r*c):return mat
        o=[]
        for i in range(m):
            mat.extend(m[i])
        mat=mat[m:]
        k=0
        for i in range(r):
            t=[]
            for j in range(c):
                x=mat[k]
                k+=1
                t.append(x)
            o.append(t)
        return o