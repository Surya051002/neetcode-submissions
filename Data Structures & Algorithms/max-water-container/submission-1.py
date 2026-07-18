class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n=len(heights)
        ans=0
        i=0
        j=n-1
        while i<j:
            val=(j-i)*min(heights[i],heights[j])
            ans=max(ans,val)
            if(heights[i]>heights[j]):
                j-=1
            else:
                i+=1


        return ans
        