class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def isValidRow(board):
            for row in board:
                if not isValid(row):
                    return False
            return True
        
        def isValidCol(board):
            for col in zip(*board):
                if not isValid(col):
                    return False
            return True
        
        def isValidSquare(board):
            for i in (0, 3, 6):
                for j in (0, 3, 6):
                    square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                    if not isValid(square):
                        return False
            return True

        def isValid(value):
            res = [i for i in value if i != "."]
            return len(res) == len(set(res))        
        
        return isValidRow(board) and isValidCol(board) and isValidSquare(board)