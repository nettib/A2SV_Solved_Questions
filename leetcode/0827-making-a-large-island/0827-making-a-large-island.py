class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        _hash = {}

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def inbound(r, c):
            return 0 <= r < n and 0 <= c < n
        

        def dfs(r, c, mark):
            grid[r][c] = mark
            _hash[mark] += 1


            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not inbound(nr, nc) or grid[nr][nc] != 1:
                    continue
                
                dfs(nr, nc, mark)

        mark = 2
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    _hash[mark] = 0
                    dfs(r, c, mark)
                    mark += 1

        
        def island_manipulate(r, c):

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not inbound(nr, nc) or grid[nr][nc] == 0:
                    continue
                temp.add(grid[nr][nc])
            

        global_max = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    temp = set()
                    island_manipulate(r, c)
                    _max = 1

                    for mark in temp:
                        _max += _hash[mark]
                    
                    global_max = max(global_max, _max)
        
        return global_max if global_max else n * n




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna