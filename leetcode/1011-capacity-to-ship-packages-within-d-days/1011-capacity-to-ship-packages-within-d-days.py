class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def fit(capacity, weights, days):
            _days = 1
            _sum = 0

            for weight in weights:
                if _sum + weight > capacity:
                    _days += 1
                    _sum = weight
                else:
                    _sum += weight
            
            return days >= _days

        l, r = max(weights), sum(weights)

        while l <= r:
            m = l + ((r - l) // 2)

            if fit(m, weights, days):
                r = m - 1
            else: 
                l = m + 1
            
        return l