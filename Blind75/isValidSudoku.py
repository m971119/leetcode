from collections import defaultdict

# class Solution:
    # def isValidSudoku(self, board: List[List[str]]) -> bool:

def isValidSudoku(board):
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        for r in range (9):
            for c in range(9):
                cell = board[r][c]
                if cell == ".":
                    continue
                if (
                    cell in rows[r]
                    or cell in cols[c]
                    or cell in squares[(r//3, c//3)]
                ):
                    return False
                cols[c].add(cell)
                rows[r].add(cell)
                squares[(r//3, c//3)].add(cell)
                
        return True

board = [["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","8",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))

"""
operator //: floor division
15 // 7 == 2
1 // 7 == 0
2 // 2 == 1
"""