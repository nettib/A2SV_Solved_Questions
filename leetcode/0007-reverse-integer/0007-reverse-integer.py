class Solution:
    def reverse(self, x: int) -> int:
        negative_checker = x < 0
        x = abs(x)
        reversed_num = 0
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        if negative_checker:
            reversed_num = - reversed_num
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        return reversed_num
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna