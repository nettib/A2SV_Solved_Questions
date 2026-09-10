class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float("inf")

        def backtrack(idx, children):
            nonlocal ans
            if max(children) >= ans:
                return
            if idx >= len(cookies):
                ans = min(ans, max(children))
                return


            for i in range(len(children)):
                children[i] += cookies[idx]
                backtrack(idx + 1, children)
                children[i] -= cookies[idx]
        
        backtrack(0, [0] * k)
        return ans




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna