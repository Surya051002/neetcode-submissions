class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left=max(nums)
        right=sum(nums)
        n=len(nums)
        ans=right

        while left<=right:
            mid=left+(right-left)//2

            count=0
            array_sum=0

            for i in range(0,n):
                array_sum+=nums[i]

                if array_sum >=mid:
                    if array_sum==mid:
                        count+=1
                        array_sum=0
                    elif array_sum-nums[i]==0:
                        count+=1
                        array_sum=0
                    else:
                        count+=1
                        array_sum=nums[i]
                if count>k:
                    break
            print(mid)
            if array_sum!=0:
                count+=1
            if count<=k:
                ans=min(mid,ans)
            if count<=k:
                right=mid-1
            else:
                left=mid+1
        return ans