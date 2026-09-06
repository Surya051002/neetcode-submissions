import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans=[]
        for i in points:
            temp=((0-i[0])**2+(0-i[1])**2)
            i.insert(0,temp)
            heapq.heappush(ans,i)
        res=[]
        while k>0:
            temp=heapq.heappop(ans)
            temp.pop(0)
            res.append(temp)
            k-=1
        return res     