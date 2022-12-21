def canConstruct( ransomNote: str, magazine: str) -> bool:
    s=set(ransomNote)
    s2=set(magazine)
    for i in ransomNote:
        if(i.count(ransomNote)>i.count(magazine)):return False
    # print(s)
    # print(s.issubset(s2))
    return True
print(canConstruct("dhru","dhuehvr"))