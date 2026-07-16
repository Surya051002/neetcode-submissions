class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={
            0:1
        }
        prefixsum=0
        ans=0
        for num in nums:
            prefixsum+=num
            if (prefixsum-k in d):
                ans+=d[prefixsum-k]
            d[prefixsum]=d.get(prefixsum,0)+1
        return ans

        