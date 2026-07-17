class Solution:
    def validPalindrome(self, s: str) -> bool:
        def fun(s):
            k=0
            l=len(s)-1

            while(k<l):
                if(s[k]!=s[l]):
                    return False
                k+=1
                l-=1
            return True

        flag=False
        i=0
        j=len(s)-1
        while i<j:
            if(s[i]!=s[j]):
                return (fun(s[i:j]) or fun(s[i+1:j+1]))
            i+=1
            j-=1
        return True
        