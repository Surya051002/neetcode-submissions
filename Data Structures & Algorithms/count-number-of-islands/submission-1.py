class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        flag=[[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def check(i,j):
            nonlocal  flag
            if i<0 or j<0:
                return 
            if (i>=len(grid) or j>=len(grid[0])) :
                return
            if flag[i][j] or grid[i][j]=="0":
                return 
            flag[i][j]=True 


            check(i+1,j)
            check(i,j+1)
            check(i-1,j)
            check(i,j-1)
        
        ans=0
        for i in range (len(grid)):
            for j in range (len(grid[0])):
                # print(flag)
                if grid[i][j]=="1" and flag[i][j]==False :
                    check(i,j)
                    ans+=1
        return ans

        