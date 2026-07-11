class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        _sum = sum(chalk)
        if k >= _sum:
            offset = k // _sum
            k -= (offset * _sum)

        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            k -= chalk[i]
        



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna