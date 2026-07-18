class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        nums.sort()
        n=len(nums)
        for i in range(0,n-3):
            if(i>0 and nums[i]==nums[i-1]):
                    continue
            for j in range(i+1,n-2):
                if(j>i+1 and nums[j]==nums[j-1]):
                    continue
                l=j+1
                r=n-1
                while l<r:
                    total=nums[i]+nums[j]+nums[l]+nums[r]
                    if(total<target):
                        l+=1
                    elif total>target:
                        r-=1
                    else:
                        ans.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        while nums[l]==nums[l-1] and l<r:
                            l+=1
        return ans      