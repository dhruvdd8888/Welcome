# class Solution:
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:

class Solution:
    # def minFallingPathSum(self, matrix) :
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def minpath(i,j):
            # print("====",matrix[i][j])
            if(i==0):return matrix[i][j]
            if(j==n-1):
                if(matrix[i-1][j]<matrix[i-1][j-1]):
                    return(minpath(i-1,j)+matrix[i][j])
                else:
                    return(minpath(i-1,j-1)+matrix[i][j])
                
            if(j==0):
                if(matrix[i-1][j]<matrix[i-1][j+1]):
                    return(minpath(i-1,0)+matrix[i][j])
                else:
                    return(minpath(i-1,1)+matrix[i][j])

            if(matrix[i-1][j]<matrix[i-1][j+1]):
                if(matrix[i-1][j]<matrix[i-1][j-1]):
                    return(minpath(i-1,j)+matrix[i][j])
                else:
                    return(minpath(i-1,j-1)+matrix[i][j])
            else:
                if(matrix[i-1][j+1]<matrix[i-1][j-1]):
                    return(minpath(i-1,j+1)+matrix[i][j])
                else:
                    return(minpath(i-1,j-1)+matrix[i][j])
        n=len(matrix)
        # ans=minpath(n-1,0)
        # print(ans)
        for i in range(n-2,-1,-1):
            for j in range(1,n-1):
                matrix[i][j]=min(matrix[i][j-1],matrix[i][j+1],matrix[i][j])
            matrix[i][0]=min(matrix[i][j+1],matrix[i][j])
            matrix[i][n-1]=min(matrix[i][j-1],matrix[i][j])

            # print(curr)
            # ans=min(ans,curr)
        return min(matrix[0])
        
s=Solution()
print(s.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))


# [100,-42,-46,-41],
#   [31,97,10,-10],
#  [-58,-51,82,89],
#   [51,81,69,-51]


[[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[51,81,69,-51]]


