class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j=len(nums)-1
        while j>0 and nums[j]==val:
            j-=1
        while i<j:
            if(nums[i]==val):
                nums[i]=nums[j]
                nums[j]=val
                while nums[j]==val:
                    j-=1
            i+=1

        return len(nums)-nums.count(val)