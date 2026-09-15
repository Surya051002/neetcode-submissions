class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=(len(nums))
        flag=[False]*n
        # print(flag)
        def findpre(i,nums,ans,flag,n):
            nonlocal res
            if len(ans)==n:
                res.append(list(ans))
            
            for ind in range(0,n):
                if flag[ind]==False:
                    flag[ind]=True
                    ans.append(nums[ind])
                    findpre(i,nums,ans,flag,n)
                    ans.pop()
                    flag[ind]=False


            
        
        findpre(0,nums,[],flag,n)
        return res

        