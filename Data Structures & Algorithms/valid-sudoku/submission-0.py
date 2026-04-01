class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap_rows = defaultdict(set)
        hashmap_cols = defaultdict(set)
        hashmap_square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if(board[r][c] == "."):
                    continue

                if (board[r][c] in hashmap_rows[r]):
                    return False
                if (board[r][c] in hashmap_cols[c]):
                    return False
                if (board[r][c] in hashmap_square[r//3, c//3]):
                    return False        
                
                hashmap_rows[r].add(board[r][c])
                hashmap_cols[c].add(board[r][c])
                hashmap_square[r //3, c//3].add(board[r][c])

        return True