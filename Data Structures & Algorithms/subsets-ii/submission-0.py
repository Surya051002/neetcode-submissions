class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=set()
        nums.sort()
        def findset(nums,ans,index):
            nonlocal res
            res.add(tuple(ans))
            if index>=len(nums):
                return 
            
            
            ans.append(nums[index])
            findset(nums,ans,index+1)
            ans.pop()
            # while index-1>-1 and nums[index-1]==nums[index]:
            #     index+=1
                
            findset(nums,ans,index+1)
        findset(nums,[],0)
        return [list(x) for x in res ]