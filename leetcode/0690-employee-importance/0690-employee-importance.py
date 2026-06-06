"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importance = defaultdict(int)
        subordinates = defaultdict(list)

        for e in employees:
            importance[e.id] = e.importance
            subordinates[e.id] = e.subordinates

        visited = set()
        total = 0

        def dfs(e):
            nonlocal total

            for nei in subordinates[e]:
                if nei in visited:
                    continue
                total += importance[nei]
                visited.add(nei)
                dfs(nei)

        total += importance[id]
        visited.add(id)
        dfs(id)

        return total
            




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna