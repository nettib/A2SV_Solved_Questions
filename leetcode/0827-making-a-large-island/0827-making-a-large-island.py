class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        

        track = {}

        def dfs(r, c):
            nonlocal _id, area
            grid[r][c] = _id
            area += 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not inbound(nr, nc) or grid[nr][nc] == 0 or (nr, nc) in visited:
                    continue
                
                visited.add((nr, nc))
                dfs(nr, nc)

        visited = set()
        _id = 2
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = 0
                    visited.add((r, c))
                    dfs(r, c)
                    track[_id] = area
                    max_area = max(max_area, area)
                    _id += 1
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    nei = set()

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if not inbound(nr, nc) or grid[nr][nc] == 0:
                            continue
                        
                        nei.add(grid[nr][nc])
                    
                    print(nei)
                    _sum = 0
                    for _id in nei:
                        _sum += track[_id]
                    
                    max_area = max(max_area, _sum + 1)
        
        return max_area

        

                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna