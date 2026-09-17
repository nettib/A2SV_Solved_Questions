class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxGold = -float("inf")

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def inbound(r, c):
            return 0 <= r < rows and 0 <= c < cols

            
        def dfs(r, c, curr):
            nonlocal maxGold

            curr += grid[r][c]
            maxGold = max(maxGold, curr)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (nr, nc) in visited or not inbound(nr, nc) or grid[nr][nc] == 0:
                    continue
                
                visited.add((nr, nc))
                dfs(nr, nc, curr)
                visited.remove((nr, nc))
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                visited = {(r, c)}
                dfs(r, c, 0)
        
        return maxGold if maxGold != -float("inf") else 0





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna