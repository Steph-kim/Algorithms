from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board[0])):
            for c in range(len(board)):
                if board[r][c] == ".":
                    continue
                
                if (board[r][c] in row[r] or
                    board[r][c] in col[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])              

        return True