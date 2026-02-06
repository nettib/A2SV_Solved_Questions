class Solution:
    def isSubset(self, a, b):
        a_hash = {}
        b_hash = {}
        
        for num in a:
            a_hash[num] = a_hash.get(num, 0) + 1
        
        for num in b:
            b_hash[num] = b_hash.get(num, 0) + 1
            
        for num in b_hash:
            if num not in a_hash or b_hash[num] > a_hash[num]:
                return False
        
        return True
