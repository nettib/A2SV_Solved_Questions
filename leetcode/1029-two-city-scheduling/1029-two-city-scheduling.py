class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []

        for i, cost in enumerate(costs):
            a, b = cost
            sep = b - a
            diff.append([sep, i])
        
        diff.sort()

        min_cost = 0

        for i in range(len(diff)):
            if i < (len(diff) // 2):
                min_cost += costs[diff[i][-1]][-1]
            else:
                min_cost += costs[diff[i][-1]][0]
        
        return min_cost
