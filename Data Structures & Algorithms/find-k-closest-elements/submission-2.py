class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n=len(arr)
        left=0
        right=n-1
        ans =-1
        res=[]
        while left<=right:
            print(left,right)
            mid=(left+right)//2
            if(arr[mid]==x):
                ans=mid
                break
            elif(arr[mid]<x):
                left=mid+1
            else:
                right=mid-1
        if(ans==-1):
            left=left-1
            right+=1
        else:
            left=ans-1
            right=ans+1
            res.append(arr[ans])
            k-=1
        while k>0:
            if(left>=0 and right<n):
                if(abs(x-arr[left])<=abs(x-arr[right])):
                    res.append(arr[left])
                    left-=1
                else:
                    res.append(arr[right])
                    right+=1
            elif(left>=0):
                res.append(arr[left])
                left-=1
            elif(right<n):
                res.append(arr[right])
                right+=1
            else:
                break
            k-=1
        res.sort()
        return res