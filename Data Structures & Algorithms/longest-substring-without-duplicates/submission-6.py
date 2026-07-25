class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=1
        i=0
        j=1
        if(s==""):
            return 0
        container={}
        container[s[i]]=0
        n=len(s)
        while j<n:
            if(s[j] in container and i<=container[s[j]]):
                
                i=container[s[j]]+1
                # container={}
                container[s[j]]=j
                length=max(length,j-(i-1))
            else:
                container[s[j]]=j
                length=max(length,j-(i-1))
                # print(s[i:j+1])

            j+=1
        length=max(length,j-(i))
        return length
        
        