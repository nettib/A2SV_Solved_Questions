class DSU:
    def __init__(self, size):
        self.parent = {i: i for i in range(size)}
        self.size = [1] * size

    def find(self, node):
        if node == self.parent[node]:
            return node
        
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, n1, n2):
        pn1 = self.find(n1)
        pn2 = self.find(n2)

        if pn1 != pn2:
            if self.size[pn1] > self.size[pn2]:
                self.parent[pn2] = pn1
                self.size[pn1] += self.size[pn2]
            else:
                self.parent[pn1] = pn2
                self.size[pn2] += self.size[pn1]
    
    def is_connected(self, n1, n2):
        return self.find(n1) == self.find(n2)

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        _id = {}

        i = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                _id[(r, c)] = i
                i += 1

        dsu = DSU(len(grid) * len(grid[0]))

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

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                _dir = directions[grid[r][c]]

                for dr, dc in _dir:
                    nr, nc = dr + r, dc + c

                    if not inbound(nr, nc):
                        continue
                    
                    _dir2 = directions[grid[nr][nc]]

                    if complement[(dr, dc)] in _dir2:
                        n1 = _id[(r, c)]
                        n2 = _id[(nr, nc)]
                        dsu.union(n1, n2)
                    
        return dsu.is_connected(_id[(0, 0)], _id[(len(grid) - 1, len(grid[0]) - 1)])




        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna