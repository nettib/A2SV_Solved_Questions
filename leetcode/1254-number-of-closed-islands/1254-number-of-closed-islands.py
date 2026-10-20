class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        # -1 - visited land

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def dfs(r, c):

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not inbound(nr, nc) or grid[nr][nc] != 0:
                    continue
                
                grid[nr][nc] = -1
                dfs(nr, nc)


        for r in [0, len(grid) - 1]:
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    grid[r][c] = -1
                    dfs(r, c)
        
        for r in range(len(grid)):
            for c in [0, len(grid[0]) - 1]:
                if grid[r][c] == 0:
                    grid[r][c] = -1
                    dfs(r, c)
        
        closed_islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    grid[r][c] = -1
                    dfs(r, c)
                    closed_islands += 1
        
        return closed_islands

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna