class Solution:
    def customSortString(self, order: str, s: str) -> str:
        track = Counter(s)
        order_set = set(order)
        ans = ""
        for char in order:
            if char in track:
                for _ in range(track[char]):
                    ans += char
        
        for char in s:
            if char not in order_set:
                ans += char

        return ans
