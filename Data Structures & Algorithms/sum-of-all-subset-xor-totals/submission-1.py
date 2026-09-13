class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        ans=0

        def findxor(nums,index,n,cur):
            
            if index>=n:
                return cur
            
            return findxor(nums,index+1,n,cur^nums[index])+findxor(nums,index+1,n,cur)
            

        return findxor(nums,0,len(nums),0)             