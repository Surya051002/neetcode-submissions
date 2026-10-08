class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        

        hashmap={}

        for i in trust:
            
            if i[1] in hashmap:
                hashmap[i[1]][0]=hashmap[i[1]][0]+1
            else:
                hashmap[i[1]]=[1,True]
            if i[0] in hashmap:
                hashmap[i[0]][1]=False
            else:
                hashmap[i[0]]=[0,False]
        print(hashmap)
        for item in hashmap.items():
            if item[1][0]==n-1 and item[1][1]:
                return item[0]
        return -1