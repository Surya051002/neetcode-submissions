class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        i=0
        j=n-1
        
        totalsum=0
        leftmax=height[i]
        rightmax=height[j]

        while i<j:
            if(leftmax<rightmax):
                # print(tempsum)
                i+=1
                leftmax=max(leftmax,height[i])
                totalsum+=leftmax-height[i]
            else:
                j-=1
                rightmax=max(rightmax,height[j])
                totalsum+=rightmax-height[j]
                
        return totalsum


        