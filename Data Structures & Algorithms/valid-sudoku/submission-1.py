class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            collection_row = set()
            for j in range(len(board)):
                row_num = board[i][j]
                if row_num != ".":
                    if row_num in collection_row:
                        return False
                collection_row.add(row_num)
        
        for k in range(len(board)):
            collection_column = set()
            for l in range(len(board)):
                column_num = board[l][k]
                if column_num != ".":
                    if column_num in collection_column:
                        return False
                collection_column.add(column_num)
        
        for m in range(0, 9, 3):
            for n in range(0, 9, 3):
                collection_square = set()
                for o in range(3):
                    for p in range(3):
                        value = board[m + o][n + p]
                        if value != ".":
                            if value in collection_square:
                                return False
                            collection_square.add(value)
        return True

        
        