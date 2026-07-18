class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        n=len(nums)
        k=n-(k%n)
        while k<n:
            temp=nums[k]
            for j in range(k,i,-1):

                nums[j]=nums[j-1]
            nums[i]=temp
            i+=1
            k+=1
        
        