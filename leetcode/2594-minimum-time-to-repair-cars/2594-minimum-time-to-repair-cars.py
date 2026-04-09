import math
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def can_repaired(t, cars, ranks):
            repaired_cars = 0

            for rank in ranks:
                repaired_cars += math.isqrt((t // rank))
            
            return repaired_cars >= cars

        l, r = 1, min(ranks) * cars * cars

        while l <= r:
            m = l + ((r - l) // 2)

            if can_repaired(m, cars, ranks):
                r = m - 1
            else:
                l = m + 1
            
        return l

