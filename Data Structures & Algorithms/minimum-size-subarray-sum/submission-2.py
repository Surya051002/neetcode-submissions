class Solution:
    def minSubArrayLen(self, target: int, arr: List[int]) -> int:
        if target in arr:
            return 1
        
        i=0
        j=1
        n=len(arr)
        sum=arr[i] 
        ans=n+1
        while j<n and i<=j:
            if(sum>=target):
                ans=min(ans,(j-i))
                sum-=arr[i]
                i+=1
            else:
                sum+=arr[j]
                j+=1
        while(sum>=target):
            ans=min(ans,j-i)
            sum-=arr[i]
            i+=1
        if ans==n+1:
            return 0
        return ans