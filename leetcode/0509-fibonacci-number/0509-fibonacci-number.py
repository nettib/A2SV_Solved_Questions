class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        data = [0] * (n + 1)

        data[0] = 0
        data[1] = 1

        for i in range(2, len(data)):
            data[i] = data[i - 1] + data[i - 2]

        return data[n]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna