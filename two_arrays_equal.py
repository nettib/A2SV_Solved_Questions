class Solution:
    def checkEqual(self, a, b) -> bool:
        a_hash = {}
        b_hash = {}
        
        for num in a:
            a_hash[num] = a_hash.get(num, 0) + 1
        
        for num in b:
            b_hash[num] = b_hash.get(num, 0) + 1
        
        return a_hash == b_hash
