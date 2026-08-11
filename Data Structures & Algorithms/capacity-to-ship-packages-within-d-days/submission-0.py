class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        max_val=sum(weights)
        right=max_val

        ans=max_val

        while left<=right:

            mid=left+(right-left)//2

            time=0
            total=0
            for i in weights:
                total+=i

                if(total>mid):
                    if(total-i!=0):
                        total-=i
                        time+=math.ceil(total/mid)
                        total=i
                    else:
                        time+=math.ceil(total/mid)
                        total=0
                
                elif total==mid:
                    total=0
                    time+=1
                print(time)
                if(time>days):
                    break

            if(total!=0):
                time+=math.ceil(total/mid)
                

            if(time<=days):
                ans=min(ans,mid)

            if(time>days):
                left=mid+1
            else:
                right=mid-1
        return ans
