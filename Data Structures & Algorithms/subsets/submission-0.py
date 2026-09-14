import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def find(nums,index,ans):
            nonlocal res
            if index>=len(nums):
                if ans not in res:
                    temp=copy.deepcopy(ans)
                    res.append(temp)
                return 
            
            
            find(nums,index+1,ans)
            ans.append(nums[index])
            find(nums,index+1,ans)
            ans.pop()



        
        
        find(nums,0,[])
        return res