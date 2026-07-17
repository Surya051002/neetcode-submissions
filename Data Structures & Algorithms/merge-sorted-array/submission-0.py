class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr1=nums1[0:m]

        i=0
        j=0
        p=0
        while i <m and j<n:
            if(arr1[i]<=nums2[j]):
                nums1[p]=arr1[i]
                i+=1
            else:
                nums1[p]=nums2[j]
                j+=1
            p+=1
        print(nums1)
        nums1[p:]=arr1[i:]
        if j<n:
            nums1[p:]=nums2[j:]    


        