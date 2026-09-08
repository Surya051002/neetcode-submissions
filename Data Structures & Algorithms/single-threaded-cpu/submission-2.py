class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        hashmap=[]
        index=0
        for task in tasks:
            hashmap.append(task)
            index+=1
        tasks.sort()
        # print(tasks)
        time=tasks[0][0]
        q=[]
        ans=[]
        taskIndex=0
        n=len(tasks)
        # print(tasks)
        while taskIndex<n or q:
            while taskIndex<n:
                if tasks[taskIndex][0]<=time:
                    heapq.heappush(q,[tasks[taskIndex][1],hashmap.index(tasks[taskIndex])])
                    # print(q)
                    taskIndex+=1
                else:
                    # print("exit")
                    break
            if q:
                temp=heapq.heappop(q)
                time+=temp[0]
                ans.append(temp[1])
            else:
                time+=1
                # print(q,time)
            # print(time)
        return ans
            
            
                

                
