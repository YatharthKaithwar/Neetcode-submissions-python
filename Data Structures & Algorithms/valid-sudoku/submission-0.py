class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range (9):
            for j in range (9):
                curr = board[i][j]
                if curr == '.':
                    continue
                


                rowID = (i, curr)
                colID = (curr, j)
                boxID = (i//3,j//3,curr)

                if rowID in seen or colID in seen or boxID in seen:
                    return False
                
                seen.add(rowID)
                seen.add(colID)
                seen.add(boxID)
        return True
        