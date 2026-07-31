class UnionFind:
    def __init__(self, size):
        self.parent = {i: i for i in range(size)}
        self.rank = [0] * size
    
    def find(self, x):
        if x == self.parent[x]:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px != py:
            if self.rank[px] == self.rank[py]:
                self.parent[py] = px
                self.rank[px] += 1
            elif self.rank[px] > self.rank[py]:
                self.parent[py] = px
            else:
                self.parent[px] = py


class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        graph = UnionFind(len(grid))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r != c and grid[r][c] == 1:
                    graph.union(r, c)
        
        track = set()
        for node in range(len(grid)):
            track.add(graph.find(node))
        
        return len(track)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna