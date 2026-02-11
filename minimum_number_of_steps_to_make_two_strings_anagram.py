class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_hash = Counter(s)
        t_hash = Counter(t)

        if s_hash == t_hash:
            return 0
        
        steps = 0
        
        for char in t_hash:
            if t_hash[char] > s_hash[char]:
                steps += t_hash[char] - s_hash[char]
        
        return steps
