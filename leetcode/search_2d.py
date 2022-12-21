def searchMatrix(matrix, target: int) -> bool:
    s=0
    e=len(matrix)-1
    while(s<=e):
        m=(s+e)//2
        print(s,m,e)
        if(matrix[m][0]<=target and (m==e or matrix[m+1][0]>target)):
            ss=0
            ee=len(matrix[0])-1
            while(ss<=ee):
                mm=(ss+ee)//2
                if(matrix[m][mm]==target):
                    print(mm)
                    return True
                elif(matrix[m][mm]>target):
                    ee=mm-1
                else:
                   ss=mm+1
            return False
        elif(matrix[m][0]>target):
            e=m-1
        else:
            s=m+1
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],90))