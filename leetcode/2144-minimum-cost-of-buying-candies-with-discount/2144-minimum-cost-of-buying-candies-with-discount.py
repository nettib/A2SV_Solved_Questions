class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)

        flag = 0
        c = 0
        for i in range(len(cost)):
            if flag == 2:
                flag = 0
                continue
            c += cost[i]
            flag += 1
        
        return c





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna