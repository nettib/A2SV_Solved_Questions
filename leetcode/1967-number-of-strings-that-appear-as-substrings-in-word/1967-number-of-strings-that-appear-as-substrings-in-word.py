class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        track = set()

        for i in range(len(word)):
            s = word[i]
            track.add(s)
            for j in range(i + 1, len(word)):
                s += word[j]
                track.add(s)
        
        ans = 0
        for pattern in patterns:
            if pattern in track:
                ans += 1
        
        return ans



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna