class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if(n==0):
            return 0
        nums.sort()
        d={}
        ans=0
        for i in nums:
            if(i-1 in d):
                d[i]=d[i-1]+1
            else:
                d[i]=1
        return max(d.values())
                
            
        