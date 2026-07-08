class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergesort(nums: List[int]) -> List[int]:
            if(len(nums)<=1):
                return nums
            n=len(nums)

            left=mergesort(nums[:n//2])
            right=mergesort(nums[n//2:])

            i=j=0
            merged=[]
            while i<len(left) and j<len(right):
                if(left[i]< right[j]):
                    merged.append(left[i])
                    i+=1
                else:
                    merged.append(right[j])
                    j+=1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged
        return mergesort(nums)

    
