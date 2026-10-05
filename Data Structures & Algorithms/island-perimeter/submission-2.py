class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        flag=[[False for _ in range(len(grid[0])) ] for _ in range(len(grid)) ]

        def find(i,j,grid):

            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or flag[i][j] or grid[i][j]==0:
                return 0

            if grid[i][j]==1:
                # print(i,j)
                flag[i][j]=True
                val=0
                if i-1<0 or grid[i-1][j]==0:
                    val+=1
                if j-1<0 or grid[i][j-1]==0:
                    val+=1
                if i+1==len(grid) or grid[i+1][j]==0:
                    val+=1
                if j+1==len(grid[0]) or grid[i][j+1]==0:
                    val+=1
                ans=val+(find(i-1,j,grid)+find(i+1,j,grid)+find(i,j-1,grid)+find(i,j+1,grid) ) 

                return ans   
            

        maxval=0

        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                
                if grid[i][j]==1:
                    temp=find(i,j,grid)
                    maxval=max(temp,maxval)
        
        return maxval
        