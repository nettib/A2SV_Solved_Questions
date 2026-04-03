class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def check(h, citations):
            l, r = 0, len(citations) - 1
            while l <= r:
                m = l + ((r - l) // 2)
                if citations[m] >= h:
                    r = m - 1
                else:
                    l = m + 1
            
            return len(citations) - l >= h

        l, r = 0, max(citations)

        while l <= r:
            m = l + ((r - l) // 2)
            if check(m, citations):
                l = m + 1
            else:
                r = m - 1
        
        return r
