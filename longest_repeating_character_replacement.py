class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_count = defaultdict(int)
        longest = 0
        maxF = 0

        l = 0
        for r in range(len(s)):
            s_count[s[r]] += 1
            maxF = max(maxF, s_count[s[r]])
            
            while (len(s[l: r + 1]) - maxF) > k:
                s_count[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
        
        return longest
