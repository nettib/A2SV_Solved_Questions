import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(k, piles):
            _h = 0

            for pile in piles:
                _h += math.ceil(pile / k)
            
            return _h <= h
        
        l = 1
        r = max(piles)

        while l <= r:
            m = l + ((r - l) // 2)
            if can_eat(m, piles):
                r = m - 1
            else:
                l = m + 1
        
        return l