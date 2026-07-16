class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        d={}
        n=len(nums)
        for num in nums:
            d[num]=0
        for i in range(1,n+1):
            if(i not in d):
                return i
        return n+1