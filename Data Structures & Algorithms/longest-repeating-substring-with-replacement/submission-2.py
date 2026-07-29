class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        d={}
        maxf=0
        l=0
        res=0

        for i in range(n):
            d[s[i]]=d.get(s[i],0)+1
            maxf=max(maxf,d[s[i]])

            while (i-l+1)-maxf>k:
                d[s[l]]-=1
                l+=1
                
            res=max(i-l+1,res)
        return res

            
                
            
            

        