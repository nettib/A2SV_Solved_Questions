class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def inbound(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])
        

        def dfs(r, c, idx):
            if board[r][c] != word[idx]:
                return False
            if idx == len(word) - 1:
                return True
            
            board[r][c] = "#"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not inbound(nr, nc) or board[nr][nc] == "#":
                    continue
                if dfs(nr, nc, idx + 1):
                    return True
            board[r][c] = word[idx]
            
            return False
        

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        
        return False


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna