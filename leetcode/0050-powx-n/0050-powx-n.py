class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def pw(x, n):
            if n == 0: return 1
            if n == 1: return x

            res = pw(x, n // 2)
            if n % 2 == 0:
                return res * res
            if n % 2 != 0:
                return x * (res * res)
        
        if n < 0:
            return 1 / pw(x, abs(n))
        return pw(x, n)
        