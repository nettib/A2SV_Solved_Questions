class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift = [0] * (len(s) + 1)

        
        for start, end, d in shifts:
            if d == 0:
                shift[start] -= 1
                shift[end + 1] += 1
            else:
                shift[start] += 1
                shift[end + 1] -= 1
        
        for i in range(1, len(shift)):
            shift[i] += shift[i - 1]
        
        res = []
        for i in range(len(s)):
            val = ord(s[i]) - ord('a')

            new_val = (val + shift[i]) % 26

            res.append(chr(new_val + ord('a')))
        
        return "".join(res)

