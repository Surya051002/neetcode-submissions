class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        piles.sort()

        left=1
        right=piles[-1]
        ans=right
        while left<=right:

            mid=left+(right-left)//2

            time=0
            for i in piles:
                if(mid>=i):
                    time+=1
                else:
                    time+=math.ceil(i/mid)
                if time>h:
                    break
            print(mid)

                
            if time>h:
                left=mid+1
            else:
                right=mid-1
                ans=min(ans,mid)
                print(ans)

                
        
        return ans
        