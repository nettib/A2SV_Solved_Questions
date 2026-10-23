class Solution:
    def dailyTemperatures(self, t: list[int]) -> list[int]:
        ans = [0] * len(t)
        stack = [0]
        
        
        for i in range(1, len(t)):

            while stack and t[stack[-1]] < t[i]:
                idx = stack.pop()
                ans[idx] = i - idx

            stack.append(i)

        return ans 



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna