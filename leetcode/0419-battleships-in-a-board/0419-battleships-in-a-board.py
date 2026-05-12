class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def inbound(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])

        visited = set()
        def dfs(node):
            r, c = node

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in visited or not inbound(nr, nc) or board[nr][nc] == ".": continue
                visited.add((nr, nc))
                dfs((nr, nc))
        
        battleships = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r, c) in visited or board[r][c] == ".": continue
                visited.add((r, c))
                dfs((r, c))
                battleships += 1
        
        return battleships


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna