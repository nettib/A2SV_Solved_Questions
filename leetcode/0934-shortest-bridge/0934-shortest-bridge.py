class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def inbound(r, c):
            return 0 <= r < n and 0 <= c < n
        
        visited = set()
        def dfs(r, c):
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in visited or not inbound(nr, nc) or not grid[nr][nc]:
                    continue
                
                dfs(nr, nc)
    
        def bfs():
            res, q = 0, deque(visited)

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if (nr, nc) in visited or not inbound(nr, nc):
                            continue
                        
                        if grid[nr][nc] == 1:
                            return res
                        
                        q.append((nr, nc))
                        visited.add((nr, nc))
                res += 1

            return res


        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs()
            






# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna