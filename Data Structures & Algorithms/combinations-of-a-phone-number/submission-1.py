class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        maps={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }


        n=len(digits)
        res=[]
        def com(n,s,arr,index):
            nonlocal maps
            
            if len(arr)==n:
                if arr:
                    res.append("".join(arr))
                return
            if index==len(s):
                return
            # print(index)
            l=maps[s[index]]
            # print(l)
            for i in range(len(l)):
                arr.append(l[i])
                com(n,s,arr,index+1)
                arr.pop()
        
        com(n,digits,[],0)
        return res
