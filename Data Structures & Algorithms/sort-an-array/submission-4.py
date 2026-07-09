class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def spl(nums,low,high):
            a=nums
            pivot = nums[low + (high - low) // 2]  
            i, j = low, high
            while True:
                while a[i] < pivot:
                    i += 1
                while a[j] > pivot:
                    j -= 1
                if i >= j:
                    return j
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
            
            
        
        def mergesort(nums: List[int],low =0 ,high=None) -> List[int]:
            
            if(high==None):
                high=len(nums)-1
            if(low>=high):
                return
            p=spl(nums,low,high)
            mergesort(nums,low,p)
            mergesort(nums,p+1,high)

        mergesort(nums)
        return nums

    
