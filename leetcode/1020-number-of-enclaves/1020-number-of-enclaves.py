class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        def at_the_edge(r, c):
            return r == 0 or r == len(grid) - 1 or c == 0 or c == len(grid[0]) - 1
        
        def dfs(r, c):
            grid[r][c] = 0

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not inbound(nr, nc) or grid[nr][nc] == 0:
                    continue

                dfs(nr, nc)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and at_the_edge(r, c):
                    dfs(r, c)
        
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    ans += 1
                
        return ans



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna