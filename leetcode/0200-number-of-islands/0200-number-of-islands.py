class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        

        def dfs(r, c):


            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not inbound(nr, nc) or (nr, nc) in visited or grid[nr][nc] == "0":
                    continue
                
                visited.add((nr, nc))
                dfs(nr, nc)
        
        visited = set()
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "0" or (r, c) in visited:
                    continue
                visited.add((r, c))
                dfs(r, c)
                islands += 1
        
        return islands


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna