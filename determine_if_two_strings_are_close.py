class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        word1_hash = {}
        word2_hash = {}

        for char in word1:
            word1_hash[char] = word1_hash.get(char, 0) + 1
        
        for char in word2:
            word2_hash[char] = word2_hash.get(char, 0) + 1

        if set(word1_hash.keys()) != set(word2_hash.keys()):
            return False
        
        if sorted(word1_hash.values()) != sorted(word2_hash.values()):
            return False

        return True
       

        
        
