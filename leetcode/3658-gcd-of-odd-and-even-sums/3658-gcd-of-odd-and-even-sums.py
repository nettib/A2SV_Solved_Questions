class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(a, b):
            if b > a:
                a, b = b, a
            
            while b > 0:
                a, b = b, a % b
            
            return a
        

        odd = 0
        even = 0

        for num in range(1, (2 * n) + 1):
            if num % 2:
                odd += num
            else:
                even += num
            
        return gcd(odd, even)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna