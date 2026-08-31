class DSU:
    def __init__(self, size):
        self.parent = {node: node for node in range(size)}
        self.size = [1] * size
    
    def get_parent(self, node):
        if self.parent[node] == node:
            return node
        
        self.parent[node] = self.get_parent(self.parent[node])
        return self.parent[node]

    def union(self, n1, n2):
        pn1 = self.get_parent(n1)
        pn2 = self.get_parent(n2)
    
        if pn1 != pn2:
            if self.size[pn1] > self.size[pn2]:
                self.parent[pn2] = pn1
                self.size[pn1] += self.size[pn2]
            else:
                self.parent[pn1] = pn2
                self.size[pn2] += self.size[pn1]
    
    def is_connected(self, n1, n2):
        pn1 = self.get_parent(n1)
        pn2 = self.get_parent(n2)
    
        return pn1 == pn2


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        dsu = DSU(n)
        for i in range(1, n):
            if abs(nums[i] - nums[i - 1]) <= maxDiff:
                dsu.union(i, i - 1)
        
        ans = []
        for n1, n2 in queries:
            ans.append(dsu.is_connected(n1, n2))
        

        return ans


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna