class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return 1
        n=x//2
        left=1
        right=n

        while left<=right:

            mid=left+(right-left)//2
            val=mid*mid
            if(val==x):
                return mid
            elif val>x:
                right=mid-1
            else:
                left=mid+1
        return left-1
        