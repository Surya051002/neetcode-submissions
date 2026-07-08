class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        j=n-1
        d={}
        while i<=j:
            if(i==j):
                return nums[i]
            if (nums[i] in d):
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
            if (nums[j] in d):
                d[nums[j]]+=1
            else:
                d[nums[j]]=1
            if(d[nums[j]]>n/2):
                return nums[j]
            if(d[nums[i]]>n/2):
                return nums[i]
            i+=1
            j-=1
        return 0
            
        