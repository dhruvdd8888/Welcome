def generate(numRows):
        def ncr(i,j):
            if(i==j or j==0):return 1
            return ans[i-1][j]+ans[i-1][j-1]
        ans=[]
        # numRows+=2
        for i in range (0,numRows):
            o=[]
            for j in range (i+1):
                o.append(ncr(i,j))
            # print(o,i)
            # if(i%2==0):o.extend(o[1::-1])
            # else:o.extend(o[::-1])
            # print(o,i)

            ans.append(o)
            print("...........",ans)
        return ans

print("\n\n\n\n\n",generate(5))