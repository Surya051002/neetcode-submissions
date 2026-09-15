class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def findcom(i,n,k,ans):
            nonlocal res
            if len(ans)==k:
                res.append(list(ans))
                return
            
            if i>n:
                return
            ans.append(i)
            findcom(i+1,n,k,ans)
            ans.pop()
            findcom(i+1,n,k,ans)
        
        findcom(1,n,k,[])

        return res
            
        