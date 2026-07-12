"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], _id: int) -> int:
        track = {}

        for employee in employees:
            track[employee.id] = employee
        
        importance = 0
        def dfs(employee):
            nonlocal importance

            importance += employee.importance

            for sub in employee.subordinates:
                dfs(track[sub])
        
        dfs(track[_id])
        return importance

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna