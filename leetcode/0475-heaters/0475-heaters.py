class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def check(r, houses, heaters):
            p1 = p2 = 0

            while p1 < len(houses) and p2 < len(heaters):
                if houses[p1] <= heaters[p2] + r and  houses[p1] >= heaters[p2] - r:
                    p1 += 1
                else:
                    p2 += 1

            return p1 == len(houses)

        houses.sort()
        heaters.sort()
        l, r = 0, max((max(houses) - min(heaters)), (max(heaters) - min(houses)))
        while l <= r:
            m = l + ((r - l) // 2)
            if check(m, houses, heaters):
                r = m - 1
            else:
                l = m + 1
        
        return l


