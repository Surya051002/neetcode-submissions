class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=len(nums1)
        m=len(nums2)
        mid=(n+m)//2
        flag=False
        if (n+m)%2==0 :
            flag=True
        
        i=0
        j=0
        arr=[]
        while i<n and j<m and i+j<=mid:
            if nums1[i]<nums2[j]:
                arr.append(nums1[i])
                i+=1
            else:
                arr.append(nums2[j])
                j+=1
        
        while i+j <=mid and i<n:
            arr.append(nums1[i])
            i+=1
        while i+j <=mid and j<m:
            arr.append(nums2[j])
            j+=1
        if (n+m)%2==0:
            return (arr[-1]+arr[-2])/2
        else:
            return arr[-1]
        