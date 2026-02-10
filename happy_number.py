class Solution:
    def isHappy(self, n: int) -> bool:
        hash_set = set()

        while n not in hash_set:
            hash_set.add(n)
            total = 0

            for num in str(n):
                total += (int(num) ** 2)
            
            n = total
            
        return n == 1

            
