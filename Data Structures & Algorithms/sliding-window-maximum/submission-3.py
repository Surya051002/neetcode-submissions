class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left=0
        right=0
        n=len(nums)
        maxd={}
        maxv=-10001
        while right<k:
            maxv=max(nums[right],maxv)
            maxd[nums[right]]=right
            right+=1
        res=[]
        res.append(maxv)

        while right<n:
            maxd[nums[right]]=right
            left+=1
            maxv=max(nums[right],maxv)
            if(maxd[maxv]>=left):
                res.append(maxv)
            elif maxd[maxv]<left :
                tempd={}
                tempmax=-10001
                for item in maxd.items():
                    if(item[1]>=left):
                        tempd[item[0]]=item[1]
                        tempmax=max(tempmax,item[0])
                maxd=tempd
                maxv=tempmax
                res.append(maxv)
            right+=1
            



            
        return res

                    

            