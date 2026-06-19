class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        q = deque([])
        visited = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    q.append((r, c))
                    visited.add((r, c))

        d = 0
        res = -1
        while q:
            d += 1

            for _ in range(len(q)):
                r, c = q.popleft()


                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (nr, nc) in visited or not inbound(nr, nc):
                        continue
                    
                    if grid[nr][nc] == 0:
                        res = d

                    visited.add((nr, nc))
                    grid[nr][nc] = 1
                    q.append((nr, nc))

        return res






# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna