class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []
        curr = []

        def backtrack(cand):
            if len(curr) == k:
                ans.append(curr[:])
                return


            for num in range(cand, n + 1):
                curr.append(num)
                backtrack(num + 1)
                curr.pop()
        
        backtrack(1)
        return ans



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna