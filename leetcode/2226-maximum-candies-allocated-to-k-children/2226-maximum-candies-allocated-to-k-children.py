class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(max_candy):
            count = 0
            for candy in candies:
                if candy >= max_candy:
                    count += (candy // max_candy)
            return count >= k


        if sum(candies) < k:
            return 0

        l, r = 1, max(candies)
        while l <= r:
            m = l + ((r - l) // 2)
            if check(m):
                l = m + 1
            else:
                r = m - 1
        
        return r
