def findSubstring(s, words) :
    ans=[]
    from itertools import permutations
    l = list(permutations(range(1,10),9))
    # for i in l:
        # ss=("".join(i))
        # if ss in s:ans.append(s.index(ss))
    return ans


s = "barfoothefoobarman"
words = ["foo","bar","cdc","foo","bar","cdc","foo","bar","cdc","foo","bar","cdc"]
print(findSubstring(s,words))