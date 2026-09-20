class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])

        def DFS(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or board[r][c]!='O':
                return
            
            board[r][c] = '#'

            DFS(r+1,c)
            DFS(r-1,c)
            DFS(r,c+1)
            DFS(r,c-1)

        for r in range(rows):
            DFS(r,0)
            DFS(r,cols-1)
        
        for c in range(cols):
            DFS(0,c)
            DFS(rows-1,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O':
                    board[r][c]='X'
                elif board[r][c]=='#':
                    board[r][c]='O'
        
        


