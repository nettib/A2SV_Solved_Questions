class Solution:
    def frequencySort(self, s: str) -> str:
        s_hash = {}
        freq_hash = {}
        ans = ""

        for char in s:
            s_hash[char] = s_hash.get(char, 0) + 1
        
        
        for char in s_hash.keys():
            freq = s_hash[char]

            if freq not in freq_hash:
                freq_hash[freq] = [char]
            else:
                freq_hash[freq].append(char)
        
        for freq in sorted(freq_hash.keys())[::-1]:
            for char in freq_hash[freq]:
                ans += freq * char

        return ans



