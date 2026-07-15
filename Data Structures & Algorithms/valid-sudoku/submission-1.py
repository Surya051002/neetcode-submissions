class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=len(board)
        m=len(board[0])
        for i in board:
            print(i)
        for i in range(0,n,3):
            for j in range(0,m,3):
                temp=set()
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if(board[k][l]!="." and (board[k][l] in temp or board[k].count(board[k][l])>1) ):
                            print("1",board[k][l])
                            return False
                        elif board[k][l]!="."  :
                            temp.add(board[k][l])
                        if(board[k][l]!="."):
                            for p in range(0,n):
                                if(p!=k and board[k][l]==board[p][l]):
                                    print(board[k][l])
                                    return False
        return True

        