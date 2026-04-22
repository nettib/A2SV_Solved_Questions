class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        visited = set()
        def dfs(grid, r, c):
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if inbound(nr, nc) and (nr, nc) not in visited and grid[nr][nc] != "0":
                    dfs(grid, nr, nc)
        

        count = 0 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(grid, r, c)
                    count += 1

        return count       