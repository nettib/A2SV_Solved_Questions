class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
            if grid[0][0] == 1 or grid[len(grid) - 1][len(grid[0]) - 1] == 1:
                return -1
            
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]

            def inbound(r, c):
                return 0 <= r < len(grid) and 0 <= c < len(grid[0])
            
            q = deque([(0, 0)])

            visited = set()
            ln = 0
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    if (r, c) == (len(grid) - 1, len(grid[0]) - 1):
                        return ln + 1

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (nr, nc) in visited or not inbound(nr, nc) or grid[r][c] == 1: continue
                        visited.add((nr, nc))
                        q.append((nr, nc))
                ln += 1
            
            return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna