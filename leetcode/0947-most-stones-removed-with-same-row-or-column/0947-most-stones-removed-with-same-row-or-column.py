class DSU:
    def __init__(self, size):
        self.parent = {i : i for i in range(size)}
        self.size = [1] * size
        self.components = size

    def find(self, stone):
        if stone == self.parent[stone]:
            return stone
        
        self.parent[stone] = self.find(self.parent[stone])
        return self.parent[stone]
    
    def union(self, s1, s2):
        ps1 = self.find(s1)
        ps2 = self.find(s2)

        if ps1 != ps2:
            self.components -= 1
            if self.size[ps1] > self.size[ps2]:
                self.parent[ps2] = ps1
                self.size[ps1] += self.size[ps2]
            else:
                self.parent[ps1] = ps2
                self.size[ps2] += self.size[ps1]
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        row = defaultdict(list)
        col = defaultdict(list)

        for stone, position in enumerate(stones):
            x, y = position

            row[x].append(stone)
            col[y].append(stone)
        
        dsu = DSU(len(stones))


        for r in row:
            for i in range(1, len(row[r])):
                dsu.union(row[r][i], row[r][i - 1])
        
        for c in col:
            for i in range(1, len(col[c])):
                dsu.union(col[c][i], col[c][i - 1])

        return len(stones) - dsu.components

        


            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna