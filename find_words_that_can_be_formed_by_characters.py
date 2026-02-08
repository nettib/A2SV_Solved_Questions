class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def check_goodness(word_hash, chars_hash):
            for char in  word_hash.keys():
                if char not in chars_hash or word_hash[char] > chars_hash[char]:
                    return False
            return True


        chars_hash = {}

        for char in chars:
            chars_hash[char] = chars_hash.get(char, 0) + 1
        
        
        res = 0
        for word in words:
            word_hash = {}
            for char in word:
                word_hash[char] = word_hash.get(char, 0) + 1

            if check_goodness(word_hash, chars_hash):
                res += len(word)
            
        return res
