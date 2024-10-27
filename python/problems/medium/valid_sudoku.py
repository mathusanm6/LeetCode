class Solution(object):
    def isValidRow(self, board):
        for row in board:
            if not self.isValid(row):
                return False
        return True

    def isValidCol(self, board):
        for col in zip(*board):
            if not self.isValid(col):
                return False
        return True

    def isValidSquare(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.isValid(square):
                    return False
        return True

    def isValid(self, cells):
        res = [i for i in cells if i != "."]
        return len(res) == len(set(res))

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        return (
            self.isValidRow(board)
            and self.isValidCol(board)
            and self.isValidSquare(board)
        )
