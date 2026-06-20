class Solution:
    def highestPeak(self, grid: List[List[int]]) -> List[List[int]]:
        height = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))] 
        

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        q = deque()
        visited = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    q.append((r, c))
                    visited.add((r, c))
        h = 0        
        while q:

            for _ in range(len(q)):
                r, c = q.popleft()
                height[r][c] = h

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (nr, nc) in visited or not inbound(nr, nc):
                        continue
                    
                    visited.add((nr, nc))
                    # height[nr][nc] = height[r][c] + 1
                    q.append((nr, nc))
            
            h += 1
        
        return height


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna