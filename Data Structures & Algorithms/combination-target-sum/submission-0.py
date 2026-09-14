import copy
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res=[]
        def findsum(nums,index,total,target,ans):
            nonlocal res
            if total==target and ans not in res:
                    temp=copy.deepcopy(ans)
                    res.append(temp)
                    return 
            if index>=len(nums) or total>target:
                return
            ans.append(nums[index])
            findsum(nums,index,total+nums[index],target,ans)
            ans.pop()
            findsum(nums,index+1,total,target,ans)

        findsum(nums,0,0,target,[])
        return res

