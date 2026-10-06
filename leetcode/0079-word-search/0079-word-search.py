class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        target = list(word)

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def inbound(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])
        
        def dfs(r, c, i):
            if i == len(target) - 1 and target[i] == board[r][c]:
                return True
            if target[i] != board[r][c]:
                return False

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not inbound(nr, nc) or (nr, nc) in visited:
                    continue
                
                visited.add((nr, nc))
                if dfs(nr, nc, i + 1):
                    return True
                
                visited.remove((nr, nc))
            
            return False

        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == target[0]:
                    visited = {(r, c)}
                    if dfs(r, c, 0):
                        return True
        
        return False
                



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna