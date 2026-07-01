class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        def cntCompleteSubstrings(s, k):
            res = 0

            for u in range(1, 27):
                window_size = u * k

                if window_size > len(s):
                    break

                char_count = Counter(s[: window_size])
                freq_count = Counter(char_count.values())



                res += (freq_count[k] == u)

                for c in range(window_size, len(s)):
                    added_char = s[c]
                    removed_char = s[c - window_size]

                    freq_count[char_count[added_char]] -= 1
                    char_count[added_char] += 1
                    freq_count[char_count[added_char]] += 1

                    freq_count[char_count[removed_char]] -= 1
                    char_count[removed_char] -= 1
                    freq_count[char_count[removed_char]] += 1

                    res += (freq_count[k] == u)
                
            return res

        start = 0
        ans = 0

        while start < len(word):
            end = start + 1
            while end < len(word) and abs(ord(word[end]) - ord(word[end - 1])) <= 2:
                end += 1
            ans += cntCompleteSubstrings(word[start: end], k)
            start = end
        
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna