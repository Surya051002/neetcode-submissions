class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre=[]
        suf=[]
        p1=1
        p2=1
        n=len(nums)
        for i in range(0,n):
            p1*=nums[i]
            pre.append(p1)
            p2*=nums[n-1-i]
            suf.append(p2)
        ans=[]
        print(pre)
        print(suf)
        for i in range(0,n):
            if(i==0):
                ans.append(suf[n-2])
            elif (i==n-1):
                ans.append(pre[i-1])
            else:
                ans.append(suf[n-i-2]*pre[i-1])

            


        return ans