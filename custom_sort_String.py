class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_count = Counter(s)
        ans = ""

        for char in order:
            if char in s_count:
                ans += (char * s_count[char])
                s_count[char] = 0
        
        for char in s_count.keys():
            if s_count[char]:
                ans += (char * s_count[char])
        
        return ans
