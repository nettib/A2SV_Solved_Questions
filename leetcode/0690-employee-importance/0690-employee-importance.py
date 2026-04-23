"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import defaultdict
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        imp = defaultdict(int)

        for employee in employees:
            i, im, s = employee.id, employee.importance, employee.subordinates
            imp[i] = im
        
        graph = defaultdict(list)
        for employee in employees:
            i, im, s = employee.id, employee.importance, employee.subordinates
            graph[i] = s
        
        total = 0
        def dfs(node):
            nonlocal total

            total += imp[node]
            for subordinate in graph[node]:
                dfs(subordinate)
        
        dfs(id)
        return total