import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

       hashmap=Counter(tasks)
       heap=[-cnt for cnt in hashmap.values()]
       heapq.heapify(heap)
       queue=deque()
       time=0
       while heap or queue:
            time+=1
            if heap:
                c=1+heapq.heappop(heap)
                if c:
                    queue.append([c,time+n])
            if queue and time==queue[0][1]:
                heapq.heappush(heap,queue.popleft()[0])
       return time
        