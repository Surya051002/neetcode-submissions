class Solution:
    def reorganizeString(self, s: str) -> str:
        hashmap=Counter(s)
        # print(hashmap)
        heap=[]
        q=[]
        for i in hashmap.items():
            temp=[-i[1],i[0]]
            heapq.heappush(heap,temp)
        
        ans=""
        flag=False

        while heap or q:
            if q:
                flag=True
            else:
                flag=False
            if heap:
                temp=heapq.heappop(heap)
                ans+=temp[1]
                if temp[0]+1<0:
                    q.append([temp[0]+1,temp[1]])
            
            if q and flag:
                heapq.heappush(heap,q.pop(0))

            if len(ans)>1 and ans[-1]==ans[-2]:
                return ""







        return ans

        
        