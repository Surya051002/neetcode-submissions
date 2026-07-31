class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashmapt={}
        for i in t:
            hashmapt[i]=hashmapt.get(i,0)+1
        left=0
        right=0
        n=len(s)
        ansval=n+1
        resans=""
        n1=len(t)
        # while right<n1:
        #     if(s[right] in hashmapt):
        #         hashmapt[s[right]]-=1
        # if(hashmapt.values()<=0):
        #     return s[left:right]
        while right<n:
            if(s[right] in hashmapt):
                hashmapt[s[right]]-=1
                while all(val<=0 for val in hashmapt.values()) and left<=right:
                    if(ansval>right-left):
                        ansval=right-left
                        resans=s[left:right+1]
                    if(s[left] in hashmapt):
                        hashmapt[s[left]]+=1
                        
                    left+=1
            right+=1
        return resans     

                    
                    




        
        