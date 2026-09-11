class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap=[]
        if a!=0:
            heapq.heappush(heap,[-a,'a'])
        if b!=0:
            heapq.heappush(heap,[-b,'b'])
        if c!=0:
            heapq.heappush(heap,[-c,'c'])
       
        heapq.heapify(heap)
        # print(heap)
        precount=[0,'d']
        ans=""
        while heap:
            print(heap,precount)
            temp=heapq.heappop(heap)
            if temp[0]<0:
                
                if precount[1]!=temp[1]:
                    precount[0]=0
                    precount[1]=temp[1]
                else:
                    precount[0]+=1
                if precount[0]>=2 and temp[1]==precount[1]:
                    if heap:
                        temp2=heapq.heappop(heap)
                        print(temp2)
                        if temp2[0]<0:
                            ans+=temp2[1]
                            precount[0]=0
                            precount[1]=temp2[1]
                            heapq.heappush(heap,[temp2[0]+1,temp2[1]])
                        heapq.heappush(heap,[temp[0],temp[1]])
                        
                    else:
                        return ans

                else:
                    ans+=temp[1]
                    heapq.heappush(heap,[temp[0]+1,temp[1]])


        return ans   
