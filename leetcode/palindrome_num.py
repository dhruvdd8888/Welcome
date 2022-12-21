def isPalindrome( x: int) -> bool:
        l=[]
        while(x):
            l.append(x%10)
            x/=10
        l2=l.copy()
        l.reverse()
        print(l,l2)
        if l2==l:return True
        return False

print(isPalindrome(121))