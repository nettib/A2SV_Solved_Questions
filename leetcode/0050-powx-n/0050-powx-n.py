class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fastPow(x, n):
            if n == 0:
                return 1
            half = fastPow(x, n // 2)  # recursive call on half
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        if n < 0:
            return 1 / fastPow(x, -n)
        else:
            return fastPow(x, n)
    