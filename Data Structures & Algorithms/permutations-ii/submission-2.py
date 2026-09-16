class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res=set()

        def findpre(nums,index):
            nonlocal res
            res.add(tuple(nums))
            if index==len(nums):
                return

            for i in range(0,len(nums)):
                if i+1<len(nums) and nums[i]==nums[i+1]:
                    continue
                nums[i],nums[index]=nums[index],nums[i]
                findpre(nums,index+1)
                nums[i],nums[index]=nums[index],nums[i]
        findpre(nums,0)
        return [list(i) for i in res]

            
        