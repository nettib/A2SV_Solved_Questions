class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        s_idx = {}

        for i, char in enumerate(s):
            if char in s_idx:
                indices = s_idx[char]
                indices.append(i)
            else:
                s_idx[char] = [i]
            
        def find_curr_char_idx(char, track_idx, prev_char_idx):
            if char not in track_idx or len(track_idx[char]) == 0:
                return -1
            
            idx_list = track_idx[char]

            l, r = 0, len(idx_list) - 1

            while l <= r:
                m = l + ((r - l) // 2)
                if idx_list[m] > prev_char_idx:
                    r = m - 1
                else:
                    l = m + 1
            
            return idx_list[l] if 0 <= l < len(idx_list) else -1
            

        
        def is_subsequence(word, s_idx):
            prev_char_idx = -1
        
            for char in word:
                curr_char_idx = find_curr_char_idx(char, s_idx, prev_char_idx)

                if curr_char_idx == -1:
                    return False
                
                prev_char_idx = curr_char_idx

            return True
        
        ans = 0
        for word in words:
            if is_subsequence(word, s_idx):
                ans += 1
        
        return ans
        





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna