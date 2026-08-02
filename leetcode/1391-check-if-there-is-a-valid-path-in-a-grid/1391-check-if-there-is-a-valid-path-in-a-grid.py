class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        UP = [-1, 0]
        DOWN = [1, 0]
        LEFT = [0, -1]
        RIGHT = [0, 1]

        complement = {(-1, 0): [1, 0], (1, 0): [-1, 0], (0, -1): [0, 1], (0, 1): [0, -1]}

        d1 = [LEFT, RIGHT]
        d2 = [UP, DOWN]
        d3 = [LEFT, DOWN]
        d4 = [RIGHT, DOWN]
        d5 = [LEFT, UP]
        d6 = [RIGHT, UP]

        directions = [0, d1, d2, d3, d4, d5, d6]

        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])


        def dfs(r, c, d):
            _dir = directions[grid[r][c]]

            if d and complement[d] not in _dir:
                return False

            visited.add((r, c))
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return True

            for dr, dc in _dir:
                nr, nc = dr + r, dc + c

                if (nr, nc) in visited or not inbound(nr, nc):
                    continue
                if dfs(nr, nc, (dr, dc)):
                    return True
            
            return False
        
        visited = set()
        return dfs(0, 0, None)
                


            





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna