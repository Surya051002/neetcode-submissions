class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        r=len(s1)
        n=len(s2)
        f=[0]*26
        for i in s1:
            f[ord(i)-97]=f[ord(i)-97]+1
        while r<=n:
            temp=f[:]
            for i in range(l,r):
                if(temp[ord(s2[i])-97]>0):
                    temp[ord(s2[i])-97]-=1
                else:
                    break
            else:
                return True
            l+=1
            r+=1
        return False       

