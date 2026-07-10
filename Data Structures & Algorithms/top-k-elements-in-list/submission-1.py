class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i, 0) + 1
        
        pq=[]
        print(d)
        def addq(item,pq):
            n=len(pq)
            for i in range(0,n):
                if(pq[i][1]>item[1]):
                    pq.insert(i,item)
                    return
            pq.append(item)
        for item in d.items():
            addq(item,pq)
        ans=[]
        print(pq)
        for i in range(len(pq)-k,len(pq)):
            ans.append(pq[i][0])
        return ans


