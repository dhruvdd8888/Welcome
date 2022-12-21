def dailyTemperatures( temperatures):
        n = len(temperatures)
        if n<=1:
            return [0]
        ans = [0]*n
        st = [0]        
        for i in range(1,n):
            while(st and temperatures[i]>temperatures[st[-1]]):
                x = st.pop()
                ans[x] = i-x
            st.append(i)
        return ans
def dailyTemperares(temperatures: list[int]) -> list[int]:
    l=[0]
    for i in range(len(temperatures)):
        if(i<=l[-1]):
            l.append(i)
        else:
            if(len(l)<0):temperatures[i]=0
            else:
                while( l[-1]<i):    
                    pass
                

print(dailyTemperatures([73,74,75,71,69,72,76,73]))

def grt(arr):

            s = [arr[0]]
            element = 0
            next = 0
            ans=[]
        
            # iterate for rest of the elements
            for i in range(1, len(arr), 1):
                next = i

                if len(s)>0:

                    # if stack is not empty, then pop an element from stack
                    element = s.pop()
        
                    '''If the popped element is smaller than next, then
                        a) print the pair
                        b) keep popping while elements are smaller and
                        stack is not empty '''
                    while element < arr[next]:
                        # next

                        # ans.append(element)
                        print(element,i,next,len(s))
                        print(arr.index(arr[next]))
                        if len(s)<1:
                            break
                        element = s.pop()
        
                    '''If element is greater than next, then push
                    the element back '''
                    if element > arr[next]:
                        # push(s, element)
                        s.append(element)
        
                '''push next to stack so that we can find
                next greater for it '''
                # push(s, next)
                s.append(arr[next])
        
            '''After iterating over the loop, the remaining
            elements in stack do not have the next greater
            element, so print -1 for them '''
            print(s)
            print(arr)
            ans.extend([0]*len(s))
            print(ans)
        

        # This code is contributed by Sunny Karira
# print(grt([73,74,75,71,69,72,76,73]))
# # print(grt([73,74,75]))
# print([1,1,4,2,1,1,0,0])




