class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        i=0
        j=n-1
        ans=[]
        while i<n-2:
            # print(nums)
            while i!=0 and i<n-2 and nums[i]==nums[i-1]:
                i+=1
            k=i+1
            j=n-1
            while k<j:
                if(nums[i]+nums[k]+nums[j]==0):
                    temp=[nums[i],nums[k],nums[j]]
                    if(temp not in ans):
                        ans.append(temp)
                    j-=1
                    k+=1
                elif(nums[i]+nums[k]+nums[j]>0):
                    j-=1
                else:
                    k+=1
            i+=1
        return ans


        
        