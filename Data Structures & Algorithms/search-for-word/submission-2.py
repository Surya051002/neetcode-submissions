class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col=len(board),len(board[0])
        flag=[[False for _ in range(col)] for _ in range(row)]
        def find(board,i,j,word,k,flag):
            if k==len(word):
                return True
            if i<0 or j<0 or i==len(board) or j==len(board[0]) or flag[i][j]==True:
                return False
            if board[i][j]==word[k]:
                flag[i][j]=True
            else:
                return False

            val=find(board,i+1,j,word,k+1,flag) or find(board,i,j+1,word,k+1,flag) or find(board,i-1,j,word,k+1,flag) or find(board,i,j-1,word,k+1,flag)
            flag[i][j]=False
            return val

        for i in range(row):
            for j in range(col):
                if board[i][j]==word[0]:
                    ans=find(board,i,j,word,0,flag)
                    if ans:
                        return ans
        return False
        
        
        