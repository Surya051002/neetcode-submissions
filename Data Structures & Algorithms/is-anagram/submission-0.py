class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        l=[0]*26
        l2=[0]*26
        for i in range(0,len(s)):
            l[ord(s[i])-97]+=1
            l2[ord(t[i])-97]+=1
        for i in range(0,26):
            if(l[i]!=l2[i]):
                return False
        return True

        