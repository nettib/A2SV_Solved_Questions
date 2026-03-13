class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []

        for i, [a_cost, b_cost] in enumerate(costs):
            diff.append([b_cost - a_cost, i])
        
        diff.sort()

        cost = 0
        for i in range(len(diff) // 2):
            cost += costs[diff[i][-1]][-1]
        
        for i in range(len(diff) // 2, len(diff)):
            cost += costs[diff[i][-1]][0]
        
        return cost