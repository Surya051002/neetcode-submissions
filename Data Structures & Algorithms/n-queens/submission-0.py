class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        flag=[[False for _ in range(n)] for _ in range(n)]
        pos=[]
        ans=[]
        def check(i,j,flag,n):
            nonlocal pos
            nonlocal ans
            # print(pos,i,j)
            if len(pos)==n:
                t=[]
                for k in range(n):
                    s=""
                    for l in range(n):
                        if  [k,l] in pos:
                            s+='Q'
                        else:
                            s+='.'
                    t.append(s)
                if t not in ans:
                    ans.append(t)

            if i==n or j==n:
                return 

            
            
            for tj in range(n):
                # print(i,tj,pos)
                if [i,tj] not in pos:
                    
                    checkpoint=True
                    for p in pos:
                        if p[0]==i or p[1]==tj:
                            checkpoint=False
                            break
                        if abs(p[0]-i) == abs(p[1]-tj):
                            checkpoint=False
                            break
                    # print(i,tj,checkpoint)
                    if checkpoint:
                        pos.append([i,tj])
                    else:
                        continue
                else:
                    continue
                check(i+1,tj,flag,n)
                if pos:
                    pos.pop()

        check(0,0,flag,n)
        
        return ans

            

        