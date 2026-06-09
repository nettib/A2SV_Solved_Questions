class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def dfs(r, c):
            nonlocal area

            area += 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (nr, nc) in visited or not inbound(nr, nc) or grid[nr][nc] == 0:
                    continue
                visited.add((nr, nc))
                dfs(nr, nc)

        visited = set()
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = 0
                    visited.add((r, c))
                    dfs(r, c)
                    max_area = max(max_area, area)

        return max_area

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna