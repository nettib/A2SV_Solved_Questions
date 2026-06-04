class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def inbound(r: int, c: int) -> bool:
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        visited = set()
        perimeter = 0

        def dfs(r, c):
            nonlocal perimeter

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in visited:
                    continue
                if not inbound(nr, nc) or grid[nr][nc] == 0:
                    perimeter += 1
                else:
                    visited.add((nr, nc))
                    dfs(nr, nc)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    visited.add((r, c))
                    dfs(r, c)
                    return perimeter


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna