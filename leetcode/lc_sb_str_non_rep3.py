def lengthOfLongestSubstring(s: str) -> int:
        ans=""
        anss=0
        for i in range(len(s)):
            print(ans)
            if(s[i] not in ans):
                ans+=s[i]
                anss=max(len(ans),anss)
            else:
                print(ans,end="---")
                t=ans.index(s[i])
                ans=ans[t+1:]+s[i]
                print(ans)

        return anss        


s="ab313136ca b  cbb"
s="ab313136ca5738  b  cbb"
s="136ca5738 ##"
s="vas"
s="s"
s=""
s="f "

print(lengthOfLongestSubstring(s))
