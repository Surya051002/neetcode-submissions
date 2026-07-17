class Solution:
    def isPalindrome(self, s: str) -> bool:

        i=0
        j=len(s)-1
        # s=set('0','1','2','3','4','5','6','7','8','9')
        while i<j:
            
            while i<j:
                if(not s[i].isalpha() and not s[i].isalnum()):
                    i+=1
                else:
                    break
            while i<j:
                if(not s[j].isalpha() and not s[j].isalnum() ):
                    j-=1
                else:
                    break
            print(i,j)
            if(i!=j and s[i].lower()!=s[j].lower()):
                return False
            else:
                i+=1
                j-=1
            
        return True

        