class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans=[]
        def create(op,cl,arr):
            nonlocal ans
            if cl==0 and op==0:
                ans.append("".join(arr))
            if cl < op:
                return
            if op>0:
                arr.append('(')
                create(op-1,cl,arr)
                arr.pop()
            if arr:
                arr.append(')')
                create(op,cl-1,arr)
                arr.pop()
        
        create(n,n,[])
        return ans
            
            