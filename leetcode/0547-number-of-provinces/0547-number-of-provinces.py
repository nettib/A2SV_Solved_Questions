class DSU:
    def __init__(self, size):
        self.parent = {i: i for i in range(size)}
        self.size = [1] * size
        self.components = size
    
    def find(self, city):
        if city == self.parent[city]:
            return city
        
        self.parent[city] = self.find(self.parent[city])
        return self.parent[city]
    
    def union(self, c1, c2):
        pc1 = self.find(c1)
        pc2 = self.find(c2)

        if pc1 != pc2:
            self.components -= 1
            if self.size[pc1] > self.size[pc2]:
                self.parent[pc2] = pc1
                self.size[pc1] += self.size[pc2]
            else:
                self.parent[pc1] = pc2
                self.size[pc2] += self.size[pc1]

class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        graph = DSU(n)

        for r in range(n):
            for c in range(n):
                if r != c and grid[r][c] == 1:
                    graph.union(r, c)
                    grid[r][c] = 0
                    grid[c][r] = 0
        
        return graph.components
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna