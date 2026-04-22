class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def inbound(r, c):
            return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])

        visited = set()
        perimeter = 0
        def dfs(grid, r, c):
            nonlocal perimeter

            visited.add((r, c))
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if not inbound(nr, nc) or grid[nr][nc] == 0:
                    perimeter += 1
                else:
                    if (nr, nc) not in visited:
                        dfs(grid, nr, nc)

        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    dfs(grid, r, c)
        
        return perimeter
                

