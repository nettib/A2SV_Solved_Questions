class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        ans = []
        path = []

        def dfs():
            if len(path) == 1 and path[0] == 0:
                return
            if len(path) > 1 and abs(path[-1] - path[-2]) != k:
                return
            if len(path) == n:
                ans.append(int("".join(str(num) for num in path[:])))
                return

            for num in range(10):
                path.append(num)
                dfs()
                path.pop()
        
        dfs()

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna