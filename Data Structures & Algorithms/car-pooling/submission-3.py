class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        heap=[(sub[1],sub) for sub in trips]

        heapq.heapify(heap)

        location =0
        c=capacity
        q=[]
        while heap:

            # print(heap)
            if q and location ==q[0][0]:
                    c+=heapq.heappop(q)[1]
            while heap and location==heap[0][0]:
                
                temp=heapq.heappop(heap)
                if c<temp[1][0]:
                    return False
                else:
                    c=c-temp[1][0]

                heapq.heappush(q,[temp[1][2],temp[1][0]])

                
            location+=1
        return True


            

        