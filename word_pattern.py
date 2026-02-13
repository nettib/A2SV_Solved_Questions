class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_letter_match = {}
        word_set = set()

        s_list = s.split(" ")

        
        if len(pattern) != len(s_list):
            return False

        for i in range(len(pattern)):
            if pattern[i] in word_letter_match and word_letter_match[pattern[i]] != s_list[i]:
                return False
            elif pattern[i] not in word_letter_match and s_list[i] in word_set:
                return False
            else:
                word_letter_match[pattern[i]] = s_list[i]
                word_set.add(s_list[i])
            
        return True
